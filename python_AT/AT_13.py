import urllib.request
from bs4 import BeautifulSoup

def raspagem():
    url = 'https://www.gutenberg.org/browse/scores/top'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
    dados_downloads = {}  # Dicionário para armazenar os dados
    
    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        extracao_tabelas = soup.find_all('table')
        
        for tabela in extracao_tabelas:
            caption = tabela.find('caption')
            
            if caption and "Downloaded Books" in caption.text:
                linhas = tabela.find_all('tr')
                for linha in linhas:
                    th = linha.find('th')
                    td = linha.find('td')
                    if th and td:
                        chave = th.text.strip()
                        valor = td.text.strip()
                        dados_downloads[chave] = valor
                break  # Encontrou a tabela certa, para o loop

        # Impressão formatada dos dados
        print("Dados de livros baixados:")
        for data, downloads in dados_downloads.items():
            print(f"{data:<15}: {downloads}")
        
        
    except Exception as e:
        print("Erro ao fazer a raspagem:", e)

        
    
raspagem()
import urllib.request
from bs4 import BeautifulSoup
import re

def resumo_top_100_baixados():
    url = 'https://www.gutenberg.org/browse/scores/top'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        
        lista_livros = soup.find_all('ol')[0]  # Busca a primeira <ol> que contém os livros
        livros = lista_livros.find_all('li')[:100]  # Pegamos os primeiros 100 livros

        # Aqui vou criar a lista formatada
        resultado = []
        for indice, livro in enumerate(livros, start=1):
            texto_completo = livro.text.strip()
            link = f"https://www.gutenberg.org{livro.a['href']}"
            
            # Usar regex para capturar o título e o número de downloads
            match = re.match(r"(.+) \((\d+)\)", texto_completo)
            if match:
                titulo = match.group(1).strip()
                downloads = match.group(2).strip()
            else:
                titulo = texto_completo
                downloads = "Desconhecido"

            resultado.append(f"{indice}. {titulo} - Downloads: {downloads}\nLink: {link}\n")

        # Exibir a saída formatada
        print("\n".join(resultado))

    except Exception as e:
        print("Houve uma falha durante a raspagem:", e)

# Executar a raspagem
resumo_top_100_baixados()

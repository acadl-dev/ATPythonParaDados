import re
import urllib.request
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com/'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
quotes = soup.find_all('div', class_='quote')

palavra_chave = "created" # Definir palavra-chave para filtrar

padrao_limpeza = re.compile(r'\b' + re.escape(palavra_chave) + r'\b', re.IGNORECASE)

# Iterar sobre citações
for quote in quotes:
    texto = quote.find('span', class_='text').text.strip()
    autor = quote.find('small', class_='author').text.strip()

    # Verifica se a palavra-chave está na citação usando regex
    if padrao_limpeza.search(texto):
        print(f'Citação (filtrada por palavra-chave "{palavra_chave}"): {texto}')
        print(f'Autor: {autor}\n')

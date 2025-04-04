import re
import urllib.request
from bs4 import BeautifulSoup


def raspagem_sem_jeito():
    url = "https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/product-reviews/1491985577/ref=cm_cr_unknown?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser") 
        
        """ Neste ponto aqui ja enfretei problemas para puxar o HTML da página, não sei ao certo se pelo fato do navegador solicitar um login antes.
        Ao tentar executar este trecho de código eu já caio no except: Erro ao raspar os dados: HTTP Error 503: Service Unavailable"""

        
        """ titulo = soup.find("span", id="productTitle")
        autor = soup.find("a", class_="a-link-normal contributorNameID")

        resultado = ""
        if titulo:
            resultado += f"Nome do Livro: {titulo.text.strip()}\n"
        else:
            resultado += "Nome do Livro: Não encontrado\n"

        if autor:
            resultado += f"Autor: {autor.text.strip()}\n"
        else:
            resultado += "Autor: Não encontrado\n" """

        print(html)

    except Exception as e:
        print("Erro ao raspar os dados:", e)


raspagem_sem_jeito()

"""
Outras dificuldades de fazer raspagem na Amazon:

1: Carregamento dinâmico de conteúdo via JavaScript, o que significa que muitas informações não estão presentes no HTML inicial, que é o que o BeautifulSoup acessa.
2: A Amazon também possui sistemas de proteção contra scraping, como detecção de bots, CAPTCHAs e redirecionamentos, dificultando o acesso automatizado.
3: URLs de avaliações geralmente carregam uma versão simplificada da página, sem detalhes completos do produto.

Como usei apenas `urllib` e `BeautifulSoup`, não consegui renderizar JavaScript.".

Soluções reais normalmente envolvem o uso de Selenium ou ferramentas que simulem um navegador.

Pesquisando na internet vi que a Amazon disponibiliza uma API própria para esse tipo de atividade
"""

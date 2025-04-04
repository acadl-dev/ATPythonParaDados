# Escreva uma função que salva uma nova lista de livros em um arquivo JSON: 
# salvar_livros_via_json(livros: list[Livro], arquivo_json: str), onde livros é a lista a ser salva e arquivo_json é o caminho para o arquivo JSON. 
# O programa deve tratar erros, como caminho inexistente. Crie o arquivo json de entrada pelo código.

import json

# Definição do tipo Livro como tupla
Livro = tuple[str, str, int]

def salvar_livros_via_json(livros: list[Livro], arquivo_json: str):
    """Salva uma lista de livros em um arquivo JSON, tratando erros de escrita."""
    try:
        # Converter a lista de tuplas para uma lista de dicionários
        livros_dict = [{"titulo": livro[0], "autor": livro[1], "ano": livro[2]} for livro in livros]

        # Salvar os livros no arquivo JSON
        with open(arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(livros_dict, arquivo, indent=4, ensure_ascii=False)

        print(f"Lista de livros salva com sucesso em {arquivo_json}")
    
    except Exception as e:
        print(f"Erro ao salvar os livros: {e}")

# Criando uma lista inicial de livros
livros_iniciais = [
    ("1984", "George Orwell", 1949),
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
]

# Caminho do arquivo JSON
arquivo_json = "biblioteca.json"

# Salvar os livros no JSON
salvar_livros_via_json(livros_iniciais, arquivo_json)

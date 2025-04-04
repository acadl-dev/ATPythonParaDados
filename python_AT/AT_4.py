# Defina uma tupla para representar um livro na biblioteca, contendo o título (string), o autor (string) e o ano de publicação (inteiro). 
# Em seguida, crie uma lista contendo pelo menos três livros.

# Definição de livros como tuplas (título, autor, ano de publicação)
livro1 = ("1984", "George Orwell", 1949)
livro2 = ("Dom Casmurro", "Machado de Assis", 1899)
livro3 = ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Lista de livros
biblioteca = [livro1, livro2, livro3]

# Exibir a lista de livros
for livro in biblioteca:
    print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

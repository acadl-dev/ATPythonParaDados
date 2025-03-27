# Escreva um programa que receba uma lista de strings representando uma lista de compras, onde cada string é um item de compra. 
# O programa deve construir um dicionário que conte quantas vezes cada item aparece e, em seguida, imprimir o dicionário.

def conta_itens(lista_compras):
    contagem = {}
    for item in lista_compras:
        item = item.lower()  # Convertendo para minúsculas
        contagem[item] = contagem.get(item, 0) + 1
    return contagem

# Exemplo de uso
lista = ["Bolo", "tomate", "Listerine", "Tomate", "Jujuba", "Melancia"]
resultado = conta_itens(lista)
print(resultado)
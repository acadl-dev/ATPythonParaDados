#Escreva uma função que recebe um dicionário de oposto e duas palavras. A função deve retornar true se as palavras forem opostas e false caso contrário.

def palavras_opostas(oposto: dict, palavra1: str, palavra2: str) -> bool:
    return oposto.get(palavra1) == palavra2 or oposto.get(palavra2) == palavra1


oposto = {
    "longe": "perto",
    "claro": "escuro",
    "alto": "baixo",
    "doce": "azedo"
}

print(palavras_opostas(oposto, "quente", "frio"))  # False
print(palavras_opostas(oposto, "claro", "escuro")) # True
print(palavras_opostas(oposto, "pequeno", "grande")) # False
print(palavras_opostas(oposto, "doce", "azedo")) # True

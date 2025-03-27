#Escreva uma função que recebe um dicionário de oposto e duas palavras. A função deve retornar true se as palavras forem opostas e false caso contrário.

def palavras_opostas(oposto: dict, palavra1: str, palavra2: str) -> bool:
    return oposto.get(palavra1) == palavra2 or oposto.get(palavra2) == palavra1

# Exemplo de uso
oposto = {
    "quente": "frio",
    "claro": "escuro",
    "grande": "pequeno",
    "feliz": "triste"
}

print(palavras_opostas(oposto, "quente", "frio"))  # True
print(palavras_opostas(oposto, "feliz", "alegre")) # False
print(palavras_opostas(oposto, "pequeno", "grande")) # True

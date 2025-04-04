# Escreva uma função que verifique se todos os caracteres de uma string estão presentes em um conjunto de caracteres fornecidos. 
# Por exemplo, para a string "casa" e o conjunto de letras "ascehgr", a função deve retornar true.

def check_caracteres(s: str, conjunto: str) -> bool:
    return set(s).issubset(set(conjunto))


print(check_caracteres("casa", "ascehgr"))  # True
print(check_caracteres("python", "ascehgr"))  # False
print(check_caracteres("python", "anshycethpgor"))  # True

# Escreva uma função que verifique se todos os caracteres de uma string estão presentes em um conjunto de caracteres fornecidos. 
# Por exemplo, para a string "casa" e o conjunto de letras "ascehgr", a função deve retornar true.

def caracteres_presentes(s: str, conjunto: str) -> bool:
    return set(s).issubset(set(conjunto))

# Exemplos de uso
print(caracteres_presentes("casa", "ascehgr"))  # True
print(caracteres_presentes("python", "ascehgr"))  # False

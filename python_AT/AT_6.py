# Implemente a seguinte função: calcular_media_idades. Essa função deve calcular e retornar a média das idades de todas as pessoas contidas no arquivo de entrada. 
# Simule os dados de entrada em um arquivo Excel com colunas de nome e idade.

def calcular_media_idades(caminho_arquivo):
    import pandas as pd

    # Lê o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Garante que a coluna 'Idade' seja numérica
    df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')

    # Remove valores ausentes ou inválidos
    df = df.dropna(subset=['Idade'])

    # Calcula e retorna a média
    return df['Idade'].mean()

nome_arquivo = "pessoas_idade.xlsx"

resultado = calcular_media_idades(nome_arquivo)
print(f"Média das idades: {resultado:.2f}")

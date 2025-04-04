# Prossiga no contexto do exercício anterior. 
# Escreva uma função para atualizar a idade de uma pessoa em uma lista, baseada no nome: atualizar_idade(pessoas: list[Pessoa], nome: str, nova_idade: int): 
# Essa função deve encontrar a pessoa pelo nome e atualizar a idade. Salve em um novo arquivo Excel. 
# Caso a pessoa não seja encontrada, a função deve exibir uma mensagem de erro.

import pandas as pd

def atualizar_idade_excel(caminho_arquivo: str, nome: str, nova_idade: int, novo_arquivo: str = 'pessoas_atualizado.xlsx'):
    try:
        # Lê o Excel original
        df = pd.read_excel(caminho_arquivo)

        # Verifica se a pessoa existe
        pessoa_encontrada = df['Nome'].str.lower() == nome.lower()

        if pessoa_encontrada.any():
            # Atualiza a idade
            df.loc[pessoa_encontrada, 'Idade'] = nova_idade

            # Salva o novo arquivo Excel
            df.to_excel(novo_arquivo, index=False)
            print(f"Idade de '{nome}' atualizada para {nova_idade}. Arquivo salvo como '{novo_arquivo}'.")
        else:
            print(f"Erro: Pessoa com nome '{nome}' não encontrada no arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
        
# Exemplo de uso
nome_arquivo = "pessoas_idade.xlsx"
atualizar_idade_excel(nome_arquivo, 'Bruno', 31)


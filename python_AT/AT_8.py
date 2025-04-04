
import csv

alunos = [
    {'Nome': 'Ana Clara', 'Idade': 20, 'Matrícula': '2023001'},
    {'Nome': 'João Pedro', 'Idade': 22, 'Matrícula': '2023002'},
    {'Nome': 'Luiza Martins', 'Idade': 19, 'Matrícula': '2023003'},
    {'Nome': 'Carlos Henrique', 'Idade': 21, 'Matrícula': '2023004'},
]


def exibir_e_salvar_alunos(alunos: list[dict], caminho_csv: str = 'alunos.csv'):
    # Exibe os alunos no console
    print("Lista de Alunos:")
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Matrícula: {aluno['Matrícula']}")

    # Tenta salvar no arquivo CSV
    try:
        with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            campos = ['Nome', 'Idade', 'Matrícula']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

            escritor.writeheader()
            for aluno in alunos:
                escritor.writerow(aluno)

        print(f"\nArquivo CSV salvo com sucesso em '{caminho_csv}'.")

    except PermissionError:
        print(f"Erro: Permissão negada ao tentar salvar o arquivo '{caminho_csv}'. Feche o arquivo se ele estiver aberto.")
    except IOError as e:
        print(f"Erro de I/O ao salvar o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


exibir_e_salvar_alunos(alunos)


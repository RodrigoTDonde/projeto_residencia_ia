import pandas as pd

# Função que tenta carregar o arquivo CSV
def carregar_dados(caminho):
    try:
        df = pd.read_csv(caminho)
        print("Arquivo carregado com sucesso!")
        return df
    except FileNotFoundError:
        print("Erro: Arquivo CSV não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None
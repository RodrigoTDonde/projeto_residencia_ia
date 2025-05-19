import pandas as pd

def verificar_falhas_multiplas(caminho_arquivo):
    # Carregando os dados
    df = pd.read_csv(caminho_arquivo)

    # Definindo colunas que representam os tipos de falha
    colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']

    # Verificando todas as colunas existem no DataFrame
    for col in colunas_falhas:
        if col not in df.columns:
            print(f"Atenção: a coluna {col} não foi encontrada no arquivo!")
            return

    # Garantindo que as colunas sejam numéricas (0 ou 1)
    df[colunas_falhas] = df[colunas_falhas].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Somando total de falhas por linha
    df['total_falhas'] = df[colunas_falhas].sum(axis=1)

    # Contando tipos de casos
    nenhuma = (df['total_falhas'] == 0).sum()
    uma = (df['total_falhas'] == 1).sum()
    multiplas = (df['total_falhas'] > 1).sum()

    # Exibindo resultados
    print(" Resultado da Verificação:")
    print(f" Linhas com 0 falhas     : {nenhuma}")
    print(f" Linhas com 1 falha      : {uma}")
    print(f" Linhas com >1 falha     : {multiplas}")

# Caminho até o CSV dentro da pasta data/
if __name__ == "__main__":
    caminho = "data/Bootcamp_train.csv"
    verificar_falhas_multiplas(caminho)
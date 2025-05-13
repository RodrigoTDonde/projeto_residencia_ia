import matplotlib.pyplot as plt

def plotar_distribuicao_falhas(df):
    """
    Gera um gráfico de barras horizontais mostrando a quantidade de cada tipo de falha.

    Parâmetros:
    df -- DataFrame que contém as colunas de falhas tratadas (0 ou 1)
    """
    colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']
    totais = df[colunas_falhas].sum().sort_values()
    
    plt.figure(figsize=(8, 5))
    totais.plot(kind='barh')
    plt.title("Distribuição de falhas nas chapas de aço")
    plt.xlabel("Quantidade de ocorrências")
    plt.ylabel("Tipo de falha")
    plt.tight_layout()
    plt.show()
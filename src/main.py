
from carregamento import carregar_dados
from preprocessamento import tratar_dados
from treinamento import treinar_modelo
from avaliacao import avaliar_modelo

# Caminho do arquivo CSV com os dados
caminho = r"data/bootcamp_train.csv"

# Passo 1 - Carregando os dados do CSV
df = carregar_dados(caminho)

# Verifica se o arquivo foi carregado corretamente
if df is not None:
    # Passo 2 - Tratamento dos dados (valores nulos, conversões, etc)
    df = tratar_dados(df)

    # Lista das colunas que indicam os tipos de falha
    colunas_falhas = [
        'falha_1', 'falha_2', 'falha_3',
        'falha_4', 'falha_5', 'falha_6', 'falha_outros'
    ]

    # Passo 3 - Treinamento do modelo com os dados limpos
    modelo, X_test, y_test, nomes_colunas = treinar_modelo(df, colunas_falhas)

    # Passo 4 - Avaliação do modelo com os dados de teste
    avaliar_modelo(modelo, X_test, y_test, nomes_colunas)
else:
    print("Encerrando execução devido a erro no carregamento dos dados.")
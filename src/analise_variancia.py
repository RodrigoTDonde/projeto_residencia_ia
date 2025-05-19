from src.carregamento import carregar_dados
from src.preprocessamento import tratar_dados

from sklearn.feature_selection import VarianceThreshold
import pandas as pd

# Caminho do arquivo de dados
caminho_csv = "data/bootcamp_train.csv"

# Carregando e tratando os dados
df = carregar_dados(caminho_csv)
df = tratar_dados(df)

# Separando variáveis de entrada (ignorando colunas de falhas e ID)
colunas_falhas = [col for col in df.columns if col.startswith('falha_')]
colunas_entrada = [col for col in df.columns if col not in colunas_falhas + ['id']]

X = df[colunas_entrada]

# Aplicando o filtro de variância
limiar = 0.01  # Variância mínima aceitável
selector = VarianceThreshold(threshold=limiar)
selector.fit(X)

# Coletando variáveis com variância abaixo do limiar
variaveis_baixa_variancia = [
    coluna for coluna, variancia in zip(X.columns, selector.variances_) if variancia < limiar
]

# Exibindo os resultados
print(f"\nNúmero total de variáveis de entrada: {len(X.columns)}")
print(f"Número de variáveis com variância < {limiar}: {len(variaveis_baixa_variancia)}\n")
print("Variáveis com baixa variância:")
for var in variaveis_baixa_variancia:
    print("-", var)
from src.carregamento import carregar_dados
from src.preprocessamento import tratar_dados
from src.visualizacao import plotar_distribuicao_falhas
from src.treinamento import treinar_modelo
from src.avaliacao import avaliar_modelo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Exibição ajustada para melhor leitura
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)
pd.set_option('display.float_format', '{:.2f}'.format)

# Função para tratar valores negativos
def tratar_valores_negativos(df):
    colunas_problema = [
        'x_minimo', 'x_maximo', 'y_minimo', 'y_maximo',
        'area_pixels', 'perimetro_x', 'perimetro_y',
        'comprimento_do_transportador', 'espessura_da_chapa_de_aço',
        'indice_de_orientaçao', 'indice_de_luminosidade'
    ]
    for coluna in colunas_problema:
        if df[coluna].lt(0).any():
            mediana = df[df[coluna] >= 0][coluna].median()
            df.loc[df[coluna] < 0, coluna] = mediana
            print(f" Corrigido: '{coluna}' - valores negativos substituídos pela mediana ({mediana:.2f})")
    return df

# Carregamento
print("\nCarregamento dos dados")
df = carregar_dados('data/Bootcamp_train.csv')
print("Dados carregados com sucesso!")
print(f"Formato do dataset: {df.shape}")

# Tratamento
print("\nTratamento dos dados")
df_tratado = tratar_dados(df)

# Correção de valores negativos
df_tratado = tratar_valores_negativos(df_tratado)
print("Dados tratados com sucesso!")

# Localização e tamanho
print("\nLocalização e tamanho")
print(df_tratado[['id', 'x_minimo', 'x_maximo', 'y_minimo', 'y_maximo']].head())

# Área e perímetro
print("\nÁrea e perímetro")
print(df_tratado[['peso_da_placa', 'area_pixels', 'perimetro_x', 'perimetro_y', 'comprimento_do_transportador']].head())

# Luminosidade
print("\nLuminosidade")
print(df_tratado[['soma_da_luminosidade', 'maximo_da_luminosidade', 'minimo_da_luminosidade']].head())

# Índices e temperatura
print("\nÍndices e temperatura")
print(df_tratado[['espessura_da_chapa_de_aço', 'temperatura',
                  'indice_de_orientaçao', 'indice_de_luminosidade',
                  'log_das_areas', 'sigmoide_das_areas']].head())

# Rótulos de falha
print("\nRótulos de falha")
colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']
print(df_tratado[colunas_falhas].head())

# Distribuição das falhas
print("\nDistribuição das falhas (quantidade de ocorrências):")
for col in colunas_falhas:
    print(f"{col}:")
    print(df_tratado[col].value_counts(), "\n")

# Valores ausentes
print("\nValores ausentes por coluna")
print(df_tratado.isnull().sum())

# Verificação de valores negativos
print("\nVerificação final – Colunas com valores negativos")
def verificar_valores_negativos(df):
    colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    negativos = (df[colunas_numericas] < 0).sum()
    negativos = negativos[negativos > 0]
    if negativos.empty:
        print("Nenhuma coluna com valores negativos.")
    else:
        print(negativos)
verificar_valores_negativos(df_tratado)

# Estatísticas descritivas
print("\nEstatísticas descritivas")
print(df_tratado.describe())

# Visualização
print("\nDistribuição das falhas")
plotar_distribuicao_falhas(df_tratado)

# Treinamento
print("\nTreinamento do modelo")
modelo, X_test, y_test, nomes_classes = treinar_modelo(df_tratado, colunas_falhas)
print("Modelo treinado com sucesso!")

# Avaliação
print("\nAvaliação por classe")
avaliar_modelo(modelo, X_test, y_test, nomes_classes)

# Gráfico: Importância das Variáveis
def plot_importancia_variaveis(modelo, X_test, salvar_em):
    importancias = [est.feature_importances_ for est in modelo.estimators_]
    media_importancia = np.mean(importancias, axis=0)
    nomes_variaveis = X_test.columns

    indices_ordenados = np.argsort(media_importancia)[::-1]
    top_n = 10
    indices_top = indices_ordenados[:top_n]

    plt.figure(figsize=(10, 6))
    plt.barh(range(top_n), media_importancia[indices_top][::-1])
    plt.yticks(range(top_n), [nomes_variaveis[i] for i in indices_top][::-1])
    plt.xlabel('Importância média')
    plt.title('Top 10 Variáveis mais Importantes')
    plt.tight_layout()

    # Garantindo que a pasta existe
    os.makedirs(os.path.dirname(salvar_em), exist_ok=True)

    plt.savefig(salvar_em)
    plt.close()
    print(f"\nGráfico de importância das variáveis salvo em: {salvar_em}")

# Caminho do gráfico gerado
caminho_grafico = 'imagens_resultados/importancia_variaveis.png'
plot_importancia_variaveis(modelo, X_test, caminho_grafico)
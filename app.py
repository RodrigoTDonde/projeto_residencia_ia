import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Título do dashboard
st.title("Dashboard de Análise de Falhas")

# Caminho do arquivo CSV com os dados
caminho = r"data/bootcamp_train.csv"

# Carregando os dados com o pandas
df = pd.read_csv(caminho)

# Lista com as colunas que representam os tipos de falhas
colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']

# Mapeando os valores de texto (ex: 'sim', 'não', 'true') para 1 e 0
mapa_binario = {
    'sim': 1, 'não': 0, 'nao': 0, 'true': 1, 'false': 0, '1': 1, '0': 0, 's': 1, 'n': 0, '-': 0
}

# Aplicando o mapeamento para cada coluna de falha
for col in colunas_falhas:
    df[col] = df[col].astype(str).str.lower().map(mapa_binario).fillna(0)

# 🔹 RESUMO DO DATASET

# Quantidade de amostras (linhas) e colunas
st.subheader("Resumo dos Dados")
st.write(f"Total de amostras: {df.shape[0]}")
st.write(f"Total de colunas: {df.shape[1]}")

# Exibindo os valores nulos por coluna (antes do tratamento)
st.subheader("Valores Nulos por Coluna")
st.dataframe(df.isnull().sum())

# 🔹 GRÁFICO DE DISTRIBUIÇÃO DAS FALHAS

# Contagem total de cada tipo de falha (quantas vezes aparece cada uma)
totais = df[colunas_falhas].sum()

# Mostrando o gráfico de barras com a contagem por tipo de falha
st.subheader("Distribuição dos Tipos de Falha")
fig, ax = plt.subplots()
totais.plot(kind='bar', color='skyblue', ax=ax)
plt.title("Quantidade por tipo de falha")
plt.xlabel("Tipo de falha")
plt.ylabel("Quantidade")
st.pyplot(fig)


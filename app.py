import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

# Título do dashboard
st.title(" Dashboard de Análise de Falhas em Chapas de Aço")

# Caminho do arquivo CSV com os dados
caminho = r"data/bootcamp_train.csv"

# Carregando os dados
df = pd.read_csv(caminho)

# Colunas que representam as classes de falha
colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']

# Mapeamento de valores inconsistentes para binário
mapa_binario = {
    'sim': 1, 'não': 0, 'nao': 0, 'true': 1, 'false': 0, '1': 1, '0': 0, 's': 1, 'n': 0, '-': 0
}
for col in colunas_falhas:
    df[col] = df[col].astype(str).str.lower().map(mapa_binario).fillna(0)

# Cria a pasta de imagens se não existir
os.makedirs("imagens_resultados", exist_ok=True)

# 🔹 RESUMO DO DATASET
st.subheader(" Resumo dos Dados")
st.write(f"Total de amostras: {df.shape[0]}")
st.write(f"Total de colunas: {df.shape[1]}")

st.subheader(" Valores Nulos por Coluna")
st.dataframe(df.isnull().sum())

# 🔹 DISTRIBUIÇÃO DAS FALHAS
st.subheader(" Distribuição dos Tipos de Falha")
totais = df[colunas_falhas].sum()

fig1, ax1 = plt.subplots()
totais.plot(kind='bar', color='skyblue', ax=ax1)
plt.title("Quantidade por tipo de falha")
plt.xlabel("Tipo de falha")
plt.ylabel("Quantidade")
st.pyplot(fig1)

# Salvar o gráfico de distribuição automaticamente
fig1.savefig("imagens_resultados/distribuicao_falhas.png")

# 🔹 IMPORTÂNCIA DAS VARIÁVEIS (IMAGEM GERADA PELO MODELO)
st.subheader(" Importância das Variáveis para o Modelo")
st.image("imagens_resultados/importancia_variaveis.png", caption="Top 10 variáveis mais importantes", use_container_width=True)

# Rodapé
st.markdown("---")
st.caption("Projeto final do Bootcamp CDIA – SENAI SC | Desenvolvido por Rodrigo Teles Dondé")

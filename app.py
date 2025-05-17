import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

# Título do dashboard
st.title("Dashboard de Análise de Falhas em Chapas de Aço")

# Caminho do arquivo CSV com os dados
caminho = r"data/bootcamp_train.csv"
df = pd.read_csv(caminho)

# Colunas de falha
colunas_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']

# Mapeiando possíveis valores binários
mapa_binario = {
    'sim': 1, 'não': 0, 'nao': 0, 'true': 1, 'false': 0, '1': 1, '0': 0, 's': 1, 'n': 0, '-': 0
}
for col in colunas_falhas:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().map(mapa_binario).fillna(0)

# Criando pasta de imagens
os.makedirs("imagens_resultados", exist_ok=True)

# Subtítulo: Visualizando
st.subheader("Amostras do Dataset")
st.dataframe(df.head())

st.subheader("Resumo dos Dados")
st.write(f"Total de amostras: {df.shape[0]}")
st.write(f"Total de colunas: {df.shape[1]}")

st.subheader("Valores Nulos por Coluna")
st.dataframe(df.isnull().sum())

# Checkbox: mostrando gráfico de distribuição
if st.checkbox("Mostrar gráfico de distribuição de falhas"):
    totais = df[colunas_falhas].sum()
    fig1, ax1 = plt.subplots()
    totais.plot(kind='bar', color='skyblue', ax=ax1)
    plt.title("Quantidade por tipo de falha")
    plt.xlabel("Tipo de falha")
    plt.ylabel("Quantidade")
    st.pyplot(fig1)
    fig1.savefig("imagens_resultados/distribuicao_falhas.png")

# Checkbox: mostrando gráfico de importância das variáveis
if st.checkbox("Mostrar gráfico de importância das variáveis"):
    st.image("imagens_resultados/importancia_variaveis.png", caption="Top 10 variáveis mais importantes", use_container_width=True)

# Filtrando interativo por falha
st.subheader("Filtrar amostras com falha específica")
falha_escolhida = st.selectbox("Escolha o tipo de falha:", colunas_falhas)
df_filtrado = df[df[falha_escolhida] == 1]
st.write(f"Amostras onde **{falha_escolhida}** está presente: {len(df_filtrado)}")
st.dataframe(df_filtrado.head())

# Filtrando por espessura mínima
if 'espessura_da_chapa_de_aço' in df.columns:
    st.subheader("Filtrar por espessura da chapa de aço")
    valor_min = st.slider("Espessura mínima", float(df['espessura_da_chapa_de_aço'].min()), float(df['espessura_da_chapa_de_aço'].max()), step=0.1)
    df_espessura = df[df['espessura_da_chapa_de_aço'] >= valor_min]
    st.write(f"Amostras com espessura >= {valor_min}: {df_espessura.shape[0]}")
    st.dataframe(df_espessura.head())

# Filtrando por ID 
st.subheader("Buscar amostra por ID")
id_busca = st.text_input("Digite um ID da amostra:")
if id_busca:
    if id_busca in df['id'].astype(str).values:
        st.success(f"Amostra com ID {id_busca} encontrada:")
        st.dataframe(df[df['id'].astype(str) == id_busca])
    else:
        st.warning("ID não encontrado no conjunto de dados.")

# Rodapé
st.markdown("---")
st.caption("Projeto final do Bootcamp CDIA – SENAI SC | Desenvolvido por Rodrigo Teles Dondé")
import pandas as pd
import joblib
from preprocessamento import tratar_dados  # Usa o mesmo tratamento do treino

# Caminhos dos arquivos
CAMINHO_TESTE = "data/bootcamp_test.csv"
CAMINHO_MODELO = "modelo_final.joblib"

# Listando colunas de falhas que o modelo prevê
colunas_falhas = [
    'falha_1', 'falha_2', 'falha_3',
    'falha_4', 'falha_5', 'falha_6', 'falha_outros'
]

# Carregando arquivo de teste 
df_teste = pd.read_csv(CAMINHO_TESTE)

# Guardando o ID das amostras 
ids = df_teste["id"]

# Tratando dados
df_teste_tratado = tratar_dados(df_teste)

# Removendo colunas de falhas
df_teste_tratado = df_teste_tratado.drop(columns=colunas_falhas, errors="ignore")

# Carregando modelo treinado salvo no arquivo
modelo = joblib.load(CAMINHO_MODELO)

# Previsões de probabilidade para cada falha
# (cada item de predicoes é um array de [prob_0, prob_1])
predicoes = modelo.predict_proba(df_teste_tratado)

# Montando um DataFrame com as probabilidades da classe positiva (1) para cada falha
predicoes_prob = pd.DataFrame({
    nome_coluna: prob[:, 1] for nome_coluna, prob in zip(colunas_falhas, predicoes)
})

# Adicionando coluna de ID ao início do DataFrame
resultado_final = pd.concat([ids.reset_index(drop=True), predicoes_prob], axis=1)

# Salvando arquivo final em formato CSV para enviar à API
resultado_final.to_csv("predicoes_para_api.csv", index=False)
print(" Arquivo 'predicoes_para_api.csv' gerado com sucesso!")
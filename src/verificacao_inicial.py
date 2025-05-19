from src.carregamento import carregar_dados
from src.preprocessamento import tratar_dados
from src.treinamento import treinar_modelo

from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    f1_score, precision_score, recall_score, classification_report
)

from xgboost import XGBClassifier

caminho_csv = "data/bootcamp_train.csv"

# Carregando e tratando dados
df = carregar_dados(caminho_csv)
df = tratar_dados(df)

# Separarando variáveis de entrada e saída
colunas_falhas = [col for col in df.columns if col.startswith('falha_')]
X = df.drop(columns=colunas_falhas + ['id'])
Y = df[colunas_falhas]

# Dividindo treino/validação
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42)

# Treinando com RandomForest
modelo_rf = MultiOutputClassifier(RandomForestClassifier(random_state=42))
modelo_rf.fit(X_train, Y_train)

# Verificações
print("\nVerificando primeiros dados do DataFrame:")
print(df.head())

print("\nVerificando shapes dos conjuntos de treino e validação:")
print("X_train:", X_train.shape)
print("X_val:", X_val.shape)
print("Y_train:", Y_train.shape)
print("Y_val:", Y_val.shape)

print("\nVerificando previsões do modelo RandomForest:")
try:
    Y_pred_rf = modelo_rf.predict(X_val)
    print("Previsões das 5 primeiras amostras:")
    print(Y_pred_rf[:5])

    # Relatório de classificação por falha (RandomForest)
    print("\nRelatório de classificação por falha (RandomForest):")
    print(classification_report(Y_val, Y_pred_rf, target_names=Y_val.columns.tolist()))

except Exception as e:
    print("Erro ao prever com o modelo RandomForest:", e)

# Treinando o modelo XGBoost
print("\nTreinando o modelo XGBoost...")

# Configurando modelo XGBoost
xgb = XGBClassifier(
    objective='binary:logistic',  # tipo de tarefa
    eval_metric='logloss',        # métrica para validação
    use_label_encoder=False,      # evita aviso desnecessário
    random_state=42
)

# Empacotando MultiOutput para prever várias falhas ao mesmo tempo
modelo_xgb = MultiOutputClassifier(xgb)

# Treinando
modelo_xgb.fit(X_train, Y_train)

# Prevendo
Y_pred_xgb = modelo_xgb.predict(X_val)

# Relatório completo por classe
print("\nRelatório de classificação por falha (XGBoost):")
print(classification_report(Y_val, Y_pred_xgb, target_names=Y_val.columns.tolist()))

# Métricas macro e micro
f1_macro = f1_score(Y_val, Y_pred_xgb, average='macro')
precision_macro = precision_score(Y_val, Y_pred_xgb, average='macro')
recall_macro = recall_score(Y_val, Y_pred_xgb, average='macro')

f1_micro = f1_score(Y_val, Y_pred_xgb, average='micro')
precision_micro = precision_score(Y_val, Y_pred_xgb, average='micro')
recall_micro = recall_score(Y_val, Y_pred_xgb, average='micro')

# Exibindo resultados
print("\nMétricas macro:")
print(f"F1-score macro: {f1_macro:.4f}")
print(f"Precisão macro: {precision_macro:.4f}")
print(f"Recall macro: {recall_macro:.4f}")

print("\nMétricas micro:")
print(f"F1-score micro: {f1_micro:.4f}")
print(f"Precisão micro: {precision_micro:.4f}")
print(f"Recall micro: {recall_micro:.4f}")
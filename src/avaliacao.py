from sklearn.metrics import accuracy_score

# Função para avaliar o modelo
def avaliar_modelo(modelo, X_test, y_test, nomes_colunas):
    # Fazendo as previsões com os dados de teste
    y_pred = modelo.predict(X_test)

    print("\nAcurácia por tipo de falha:")
    for i, col in enumerate(nomes_colunas):
        acc = accuracy_score(y_test[col], y_pred[:, i])
        print(f"{col}: {acc:.2f}")
from sklearn.metrics import accuracy_score, classification_report

# Avaliar o modelo
def avaliar_modelo(modelo, X_test, y_test, nomes_colunas):
    # Previsões com os dados de teste
    y_pred = modelo.predict(X_test)

    print("\n Avaliação por tipo de falha:\n")

    for i, col in enumerate(nomes_colunas):
        print(f"--- {col} ---")
        
        acc = accuracy_score(y_test[col], y_pred[:, i])
        print(f"Acurácia: {acc:.2f}")

        # Métricas detalhadas
        print(classification_report(
            y_test[col], y_pred[:, i],
            zero_division=0, digits=2
        ))
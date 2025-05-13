from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

# Função para treinar o modelo
def treinar_modelo(df, colunas_falhas):
    # Separa os dados de entrada (X) e os rótulos (y)
    X = df.drop(columns=colunas_falhas)
    y = df[colunas_falhas]

    # Separa em dados de treino e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Cria o modelo Random Forest para múltiplas saídas
    modelo = MultiOutputClassifier(RandomForestClassifier(random_state=42))

    # Treina o modelo
    modelo.fit(X_train, y_train)

    # Retorna o modelo e os dados de teste
    return modelo, X_test, y_test, y.columns
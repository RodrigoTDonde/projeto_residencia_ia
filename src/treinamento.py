from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from imblearn.over_sampling import RandomOverSampler
import pandas as pd

def treinar_modelo(df, colunas_falhas):
    # Divide X e y
    X = df.drop(columns=colunas_falhas)
    y = df[colunas_falhas]

    # Divide treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Inicializa listas
    X_train_bal = []
    y_train_bal = []

    for coluna in colunas_falhas:
        ros = RandomOverSampler(random_state=42)
        X_res, y_res = ros.fit_resample(X_train, y_train[coluna])

        # Adiciona X_res
        X_train_bal.append(pd.DataFrame(X_res, columns=X.columns))

        # Cria um DataFrame com a coluna atual e as outras como 0
        y_res_df = pd.DataFrame(0, index=range(len(y_res)), columns=colunas_falhas)
        y_res_df[coluna] = y_res

        # Adiciona y_res_df
        y_train_bal.append(y_res_df)

    # Concatena tudo
    X_train_final = pd.concat(X_train_bal, ignore_index=True)
    y_train_final = pd.concat(y_train_bal, ignore_index=True)

    # Garante a ordem das colunas
    y_train_final = y_train_final[colunas_falhas]

    # Cria e treina o modelo
    modelo = MultiOutputClassifier(RandomForestClassifier(random_state=42))
    modelo.fit(X_train_final, y_train_final)

    return modelo, X_test, y_test, colunas_falhas
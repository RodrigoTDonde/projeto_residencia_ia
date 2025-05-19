import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

f1_rf = {
    "falha_1": 0.08,
    "falha_2": 0.37,
    "falha_3": 0.90,
    "falha_4": 0.82,
    "falha_5": 0.25,
    "falha_6": 0.42,
    "falha_outros": 0.46
}

f1_xgb = {
    "falha_1": 0.42,
    "falha_2": 0.48,
    "falha_3": 0.62,
    "falha_4": 0.67,
    "falha_5": 0.48,
    "falha_6": 0.48,
    "falha_outros": 0.49
}

df_comparacao = pd.DataFrame({
    "Random Forest": f1_rf,
    "XGBoost": f1_xgb
})

df_comparacao.plot(kind="bar", figsize=(10, 6), rot=45)
plt.title("Comparação de F1-score por Classe de Falha")
plt.ylabel("F1-score")
plt.xlabel("Classe de Falha")
plt.ylim(0, 1)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(title="Modelos")
plt.tight_layout()
plt.show()

# 🚀 Projeto: Classificação de Defeitos em Chapas de Aço

Este projeto foi desenvolvido como parte do **Bootcamp de Ciência de Dados – SENAI SC**.  
Seu objetivo é criar um sistema inteligente que identifique automaticamente o tipo de defeito em chapas de aço inox, a partir de **31 indicadores** extraídos de imagens da superfície.

---

## 🛠️ O que o projeto faz

- 📥 Carrega os dados de um arquivo CSV  
- 🧼 Limpa e prepara os dados para o modelo  
- 🧠 Treina um modelo para prever o tipo de defeito  
- 🔁 Compara o desempenho entre RandomForest e XGBoost  
- 📊 Avalia e apresenta os resultados do modelo por classe  
- 🧪 Realiza análise de variância para refinar os atributos  
- 🖼️ Visualizações são geradas via código e salvas manualmente para uso em apresentação  
- 🌐 Exibe um **dashboard interativo** no navegador  

---

## 📁 Estrutura das pastas

```text
projeto_residencia_ia/
├── data/                     → Arquivo de dados CSV
├── imagens_resultados/       → Gráficos gerados automaticamente ou manualmente
├── src/                      → Código principal do projeto
│   ├── main.py               → Script principal
│   ├── carregamento.py       → Leitura dos dados
│   ├── preprocessamento.py   → Limpeza e tratamento
│   ├── treinamento.py        → Treinamento do modelo
│   ├── avaliacao.py          → Avaliação do modelo
│   ├── verificacao_inicial.py → Comparação RandomForest x XGBoost
│   ├── comparacao_grafico.py → Gráfico comparativo de desempenho
│   └── analise_variancia.py  → Identificação de variáveis com baixa variância
├── app.py                    → Dashboard em Streamlit
├── avaliacoes/               → Métricas da API oficial
├── requirements.txt          → Bibliotecas utilizadas
└── README.md                 → Este documento
```

---

## 🖥️ Como rodar o projeto no seu computador

🔹 1. Clonar o repositório
```bash
git clone https://github.com/RodrigoTDonde/projeto_residencia_ia.git
cd projeto_residencia_ia
```

🔹 2. Criar ambiente virtual
```bash
python -m venv .venv
```

🔹 3. Ativar ambiente virtual (Windows)
```bash
.venv\Scripts\activate
```
⚠️ Se estiver usando PowerShell, execute antes:
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
```

🔹 4. Instalar dependências
```bash
pip install -r requirements.txt
```

🔹 5. Executar o script principal
```bash
python src/main.py
```

🔹 6. Iniciar o dashboard interativo
```bash
streamlit run app.py
```
Acesse em: http://localhost:8501

---

## ✅ Resultados do modelo (avaliação local)

```text
falha_1: 93%
falha_2: 94%
falha_3: 96%
falha_4: 99%
falha_5: 98%
falha_6: 78%
falha_outros: 74%
```

---

## 📊 Avaliação Final na API

O modelo foi testado usando os dados ocultos fornecidos pela API oficial do desafio.  
Os principais resultados foram:

- 🎯 Macro Accuracy: 85,82%  
- 📈 Macro ROC AUC: 0,89  
- 🥇 F1-Score mais alto: 0,20 (Classe 5)

📁 Arquivo com métricas salvo em:  
`avaliacoes/metrics_resultado_api.json`

---

## 🔍 Verificação de múltiplas falhas por amostra

Foi criado um script dedicado (`verificar_multiplas_falhas.py`) para verificar se uma mesma amostra poderia apresentar mais de um tipo de falha simultaneamente.

Resultado:

- 🟡 Linhas com 0 falhas: 1923  
- 🟢 Linhas com 1 falha: 1467  
- 🔴 Linhas com mais de 1 falha: 0  

**Conclusão**: Nenhuma amostra no dataset apresenta múltiplas falhas.  
Mesmo assim, optamos por modelar o problema como multirrótulo, utilizando `MultiOutputClassifier`, garantindo flexibilidade, clareza por classe e compatibilidade com a avaliação via API.

---

## 📌 Etapas Concluídas no Projeto

📂 Estrutura  
- Organização em pastas (`data`, `src`, `imagens_resultados`, `avaliacoes`)  
- Modularização com scripts reutilizáveis  

🧪 Análise e Modelagem  
- Tratamento de valores nulos e negativos  
- Balanceamento com `RandomOverSampler`  
- Modelo multirrótulo com `RandomForestClassifier` + `MultiOutputClassifier`  
- Inclusão do modelo `XGBoost` e comparação com RandomForest  
- Avaliação por classe (relatórios e métricas macro/micro)  
- Análise de variância com `VarianceThreshold`  
- Geração de gráfico comparativo F1-score entre os modelos  

📄 Resultados  
- Geração do arquivo `modelo_final.joblib`  
- Predição com `bootcamp_test.csv`  
- Exportação do arquivo `predicoes_para_api.csv`  

📊 Dashboard  
- Desenvolvido com Streamlit  
- Gráficos: distribuição de falhas, importância das variáveis, comparação entre modelos  
- Filtros interativos: por falha, ID, espessura e checkboxes  

📄 Documentação  
- README.md completo e explicativo  
- Instruções passo a passo para execução local  
- Interpretação clara dos resultados

---

🙋‍♂️ Desenvolvido por  
**Rodrigo Teles Dondé**  
Projeto final do Bootcamp CDIA – SENAI SC

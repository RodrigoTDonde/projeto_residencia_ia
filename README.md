---

# 🚀 Projeto: Classificação de Defeitos em Chapas de Aço

Este projeto foi desenvolvido como parte do **Bootcamp de Ciência de Dados – SENAI SC**.  
Seu objetivo é criar um sistema inteligente que identifique automaticamente o tipo de defeito em chapas de aço inox, a partir de **31 indicadores** extraídos de imagens da superfície.

---

## 🛠️ O que o projeto faz

- 📥 Carrega os dados de um arquivo CSV  
- 🧼 Limpa e prepara os dados para o modelo  
- 🧠 Treina um modelo para prever o tipo de defeito  
- 📊 Avalia e apresenta os resultados do modelo  
- 🖼️ Gera gráficos automaticamente  
- 🌐 Exibe um **dashboard interativo** no navegador  

---

## 📁 Estrutura das pastas

```text
projeto_residencia_ia/
├── data/                     → Arquivo de dados CSV
├── imagens_resultados/       → Gráficos gerados automaticamente
├── src/                      → Código principal do projeto
│   ├── main.py               → Script principal
│   ├── carregamento.py       → Leitura dos dados
│   ├── preprocessamento.py   → Limpeza e tratamento
│   ├── treinamento.py        → Treinamento do modelo
│   └── avaliacao.py          → Avaliação do modelo
├── app.py                    → Dashboard em Streamlit
├── avaliacoes/               → Métricas da API oficial
├── requirements.txt          → Bibliotecas utilizadas
└── README.md                 → Este documento
🖥️ Como rodar o projeto no seu computador
🔹 1. Clonar o repositório
sh
Copiar
Editar
git clone https://github.com/RodrigoTDonde/projeto_residencia_ia.git
cd projeto_residencia_ia
🔹 2. Criar ambiente virtual
sh
Copiar
Editar
python -m venv .venv
🔹 3. Ativar ambiente virtual (Windows)
sh
Copiar
Editar
.venv\Scripts\activate
⚠️ Se estiver usando PowerShell, execute antes:

sh
Copiar
Editar
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
🔹 4. Instalar dependências
sh
Copiar
Editar
pip install -r requirements.txt
🔹 5. Executar o script principal
sh
Copiar
Editar
python src/main.py
🔹 6. Iniciar o dashboard interativo
sh
Copiar
Editar
streamlit run app.py
Acesse em: http://localhost:8501

✅ Resultados do modelo (avaliação local)
makefile
Copiar
Editar
falha_1: 93%
falha_2: 94%
falha_3: 96%
falha_4: 99%
falha_5: 98%
falha_6: 78%
falha_outros: 74%
📊 Avaliação Final na API
O modelo foi testado usando os dados ocultos fornecidos pela API oficial do desafio.
Os principais resultados foram:

🎯 Macro Accuracy: 85,82%

📈 Macro ROC AUC: 0,89

🥇 F1-Score mais alto: 0,20 (Classe 5)

📁 Arquivo com métricas salvo em:
avaliacoes/metrics_resultado_api.json

📌 Etapas Concluídas no Projeto
📂 Estrutura
Organização em pastas (data, src, imagens_resultados, avaliacoes)

Modularização com scripts reutilizáveis

🧪 Análise e Modelagem
Tratamento de valores nulos e negativos

Balanceamento com RandomOverSampler

Modelo multirrótulo com RandomForestClassifier + MultiOutputClassifier

Avaliação por classe

Geração do arquivo modelo_final.joblib

Predição com bootcamp_test.csv

Exportação do arquivo predicoes_para_api.csv

🔍 Validação Final
Envio das predições para a API oficial

Métricas avaliadas com sucesso

JSON salvo em avaliacoes/

📊 Dashboard
Desenvolvido com Streamlit

Gráficos: distribuição de falhas, importância das variáveis

Filtros interativos: por falha, ID, espessura e checkboxes

📄 Documentação
README.md completo e explicativo

Instruções passo a passo para execução local

Interpretação clara dos resultados

🙋‍♂️ Desenvolvido por
Rodrigo Teles Dondé
Projeto final do Bootcamp CDIA – SENAI SC
---

# Projeto: Classificação de Defeitos em Chapas de Aço

Este projeto foi feito para o Bootcamp de Ciência de Dados – SENAI SC.  
O objetivo é treinar um modelo que identifica automaticamente o tipo de defeito em uma chapa de aço inox, com base em 31 indicadores extraídos de imagens da superfície das chapas.

---

## 🔧 O que o projeto faz

* Carrega os dados de um arquivo CSV
* Limpa os dados e prepara para o modelo
* Treina um modelo para prever o tipo de defeito
* Mostra os resultados e a acurácia do modelo
* Salva automaticamente os gráficos gerados
* Exibe um dashboard interativo com gráficos no navegador

---

## 🗂️ Estrutura das pastas

```text
projeto_residencia_ia/
├── data/                     → Onde está o arquivo de dados CSV
├── imagens_resultados/       → Onde ficam os gráficos gerados automaticamente
├── src/                      → Onde está o código principal do projeto
│   ├── main.py               → Código principal que roda tudo
│   ├── carregamento.py       → Carrega os dados
│   ├── preprocessamento.py   → Limpa e trata os dados
│   ├── treinamento.py        → Treina o modelo de machine learning
│   └── avaliacao.py          → Mostra o resultado (acurácia)
├── app.py                    → Exibe o dashboard interativo com Streamlit
├── avaliacoes/               → Métricas finais obtidas na API oficial
├── requirements.txt          → Lista de bibliotecas usadas
└── README.md                 → Explicação do projeto
▶️ Como rodar o projeto no seu computador
1. Clonar o projeto
sh
Copiar
Editar
git clone https://github.com/RodrigoTDonde/projeto_residencia_ia.git
cd projeto_residencia_ia
2. Criar ambiente virtual
sh
Copiar
Editar
python -m venv .venv
3. Ativar o ambiente virtual (Windows)
sh
Copiar
Editar
.venv\Scripts\activate
⚠️ Se estiver usando PowerShell e aparecer erro de permissão, execute:

sh
Copiar
Editar
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
4. Instalar as dependências
sh
Copiar
Editar
pip install -r requirements.txt
5. Rodar o código principal
sh
Copiar
Editar
python src/main.py
6. Ver o dashboard (gráficos no navegador)
sh
Copiar
Editar
streamlit run app.py
Acesse: http://localhost:8501

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
O modelo foi testado com os dados ocultos pela API oficial do desafio. Os principais resultados foram:

Macro Accuracy: 85,82%

Macro ROC AUC: 0,89

F1-Score mais alto: 0,20 (Classe 5)

Apesar do bom desempenho médio, os resultados por classe mostraram baixa precisão para detectar classes de falha minoritárias, refletindo o desbalanceamento nos dados.

As métricas completas estão disponíveis no arquivo:

bash
Copiar
Editar
avaliacoes/metrics_resultado_api.json
✅ Etapas Concluídas no Projeto
📁 Estrutura do Projeto

Organização em pastas (data, src, imagens_resultados, avaliacoes)

Código modularizado: carregamento.py, preprocessamento.py, treinamento.py, avaliacao.py, main.py

📊 Análise e Modelagem

Tratamento de valores nulos e negativos

Balanceamento das classes com RandomOverSampler

Modelo multirrótulo com RandomForestClassifier + MultiOutputClassifier

Avaliação local com métricas por tipo de falha

Salvamento do modelo em modelo_final.joblib

Geração de predições com bootcamp_test.csv

Geração do arquivo predicoes_para_api.csv

🧪 Validação Final

Envio das predições para a API oficial

Métricas avaliadas com sucesso: Macro Accuracy: 85,82%, AUC: 0.89

JSON com as métricas salvo na pasta avaliacoes/

📊 Dashboard

Dashboard com Streamlit funcionando

Visualizações dinâmicas: distribuição de falhas, importância de variáveis

Filtros interativos: por falha, ID, espessura, checkboxes

📄 Documentação

README.md bem estruturado e técnico

Instruções para execução local

Seção de avaliação final da API com interpretação

🙋‍♂️ Feito por
Rodrigo Teles Dondé
Projeto final do Bootcamp CDIA – SENAI SC


---

# Projeto: Classificação de Defeitos em Chapas de Aço

Este projeto foi feito para o bootcamp de Ciência de Dados.
O objetivo é treinar um modelo que identifica automaticamente o tipo de defeito em uma chapa de aço inox, usando medidas que foram tiradas de um modelo de  chapa de aço.

---

## 🔧 O que o projeto faz

* Carrega os dados de um arquivo CSV
* Limpa os dados e prepara para o modelo
* Treina um modelo para prever o tipo de defeito
* Mostra os resultados e a acurácia do modelo
* Exibe um dashboard com gráfico no navegador

---

## 🗂️ Estrutura das pastas

```
projeto_residencia_ia/
├── data/                  → Onde está o arquivo de dados CSV
├── src/                   → Onde está o código principal do projeto
│   ├── main.py            → Código principal que roda tudo
│   ├── carregamento.py    → Carrega os dados
│   ├── preprocessamento.py→ Limpa e trata os dados
│   ├── treinamento.py     → Treina o modelo de machine learning
│   └── avaliacao.py       → Mostra o resultado (acurácia)
├── app.py                 → Mostra o gráfico em forma de dashboard
├── requirements.txt       → Lista de bibliotecas usadas
└── README.md              → Explicação do projeto
```

---

## ▶️ Como rodar o projeto no seu computador

### 1. Clonar o projeto

```bash
git clone https://github.com/RodrigoTDonde/projeto_residencia_ia.git
cd projeto_residencia_ia
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual (Windows)

```bash
.venv\Scripts\activate
```

> ⚠️ Se estiver usando PowerShell e aparecer erro de permissão, execute:
>
> ```bash
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> .venv\Scripts\Activate.ps1
> ```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Rodar o código principal

```bash
python src/main.py
```

### 6. Ver o dashboard (gráfico no navegador)

```bash
streamlit run app.py
```

Acesse: [http://localhost:8501](http://localhost:8501)

---

## ✅ Resultados do modelo

```
falha_1: 93%
falha_2: 94%
falha_3: 96%
falha_4: 99%
falha_5: 98%
falha_6: 78%
falha_outros: 74%
```

---

## 🙋‍♂️ Feito por

**Rodrigo Teles Dondé**
Projeto final do Bootcamp CDIA – SENAI SC

---




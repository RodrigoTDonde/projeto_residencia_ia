import pandas as pd

def tratar_dados(df):
    # Tratando colunas com valores nulos (NaN)
    colunas_com_nulos = [
        'x_maximo', 'soma_da_luminosidade', 'maximo_da_luminosidade',
        'espessura_da_chapa_de_aço', 'index_quadrado',
        'indice_global_externo', 'indice_de_luminosidade'
    ]

    for coluna in colunas_com_nulos:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce').fillna(df[coluna].astype(float).mean())

    # Convertendo colunas de falhas para 0 e 1
    colunas_falhas = [
        'falha_1', 'falha_2', 'falha_3',
        'falha_4', 'falha_5', 'falha_6', 'falha_outros'
    ]

    # Mapeando textos como 'sim', 'não', 'true', etc., para números
    mapa_binario = {
        'sim': 1, 'não': 0, 'nao': 0, 'true': 1, 'false': 0,
        '1': 1, '0': 0, 's': 1, 'n': 0, '-': 0
    }

    for col in colunas_falhas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().map(mapa_binario).fillna(0).astype(int)

    # Corrigindo outras colunas que contêm texto e deveriam ser numéricas
    colunas_com_texto = [
        'tipo_do_aço_A300', 'tipo_do_aço_A400',
        'temperatura', 'indice_de_variacao_x', 'indice_de_variacao_y'
    ]

    for col in colunas_com_texto:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Trata valores negativos em colunas onde não fazem sentido
    colunas_sem_negativos = [
        'x_minimo', 'x_maximo', 'y_minimo', 'y_maximo',
        'area_pixels', 'perimetro_x', 'perimetro_y',
        'comprimento_do_transportador', 'espessura_da_chapa_de_aço',
        'indice_de_orientaçao', 'indice_de_luminosidade'
    ]

    for coluna in colunas_sem_negativos:
        if coluna in df.columns:
            mediana = df[coluna].median()
            df[coluna] = df[coluna].apply(lambda x: x if x >= 0 else mediana)

    return df
import pandas as pd

# Dados processados pelo modelo (amostra final)
data = {
    'ID_PRODUTO': [1, 1, 1, 1, 1],
    'DIA': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
    'FLAG_PROMOCAO': [0, 0, 0, 1, 0],
    'QUANTIDADE_ESTOQUE': [18, 14, 22, 0, 0],
    'PREVISAO_ESTOQUE': [19.42, 15.10, 21.05, 1.22, 0.45]
}

df_final = pd.DataFrame(data)
df_final.to_csv('previsoes_estoque_finais.csv', index=False)
print("Arquivo salvo com sucesso!")

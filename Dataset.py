import pandas as pd
import numpy as np

df = pd.read_csv('USAccidents/US_Accidents_March23.csv')

# Embaralha os dados para garantir aleatoriedade
df_embaralhado = df.sample(frac=1, random_state=42)

# Divide em 10 partes aproximadamente iguais
amostras = np.array_split(df_embaralhado, 10)

# Salva cada amostra em um arquivo CSV separado
for i, amostra in enumerate(amostras):
    amostra.to_csv(f'USAccidents_amostra_{i+1}.csv', index=False)

print("Divisão concluída com sucesso!")
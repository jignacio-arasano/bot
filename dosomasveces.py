import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('numeros_telefonicos.xlsx', header=None, names=['Numero'])

# Encuentra los números que aparecen dos veces o más
numeros_repetidos = df['Numero'].value_counts()
numeros_repetidos = numeros_repetidos[numeros_repetidos >= 2]

# Crea un nuevo DataFrame con los números repetidos
df_result = pd.DataFrame(numeros_repetidos.index.tolist(), columns=['Numero'])

# Guarda el DataFrame en un nuevo archivo de Excel
df_result.to_excel('numeros_repetidos.xlsx', index=False)


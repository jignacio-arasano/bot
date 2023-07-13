import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('v2.xlsx', header=None, names=['Telefono'])

# Encuentra los números telefónicos únicos
numeros_unicos = df['Telefono'][~df['Telefono'].duplicated(keep=False)]

# Crea un nuevo DataFrame con los números únicos
df_result = pd.DataFrame(numeros_unicos, columns=['Telefono'])

# Guarda el DataFrame en un nuevo archivo de Excel
df_result.to_excel('v3.xlsx', index=False)








import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('v3.xlsx', header=None, names=['Telefono'])

# Encuentra los números telefónicos que aparecen dos veces
numeros_repetidos = df['Telefono'][df['Telefono'].duplicated(keep=False)]

# Encuentra los números telefónicos únicos que aparecen dos veces
numeros_unicos_dos_veces = numeros_repetidos[numeros_repetidos.duplicated()]

# Crea un nuevo DataFrame con los números únicos que aparecen dos veces
df_result = pd.DataFrame(numeros_unicos_dos_veces, columns=['Telefono'])

# Guarda el DataFrame en un nuevo archivo de Excel
df_result.to_excel('v4.xlsx', index=False)

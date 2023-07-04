import pandas as pd
import re

# Ruta del archivo de entrada
archivo_entrada = 'dimaria.xlsx'

# Ruta del archivo de salida
archivo_salida = 'dimaria7.xlsx'

# Columna a limpiar (indexada en base 0)
columna_limpiar = 0

# Leer archivo de entrada
df = pd.read_excel(archivo_entrada)

# Obtener los datos de la columna a limpiar
columna_datos = df.iloc[:, columna_limpiar]

# Eliminar el texto de cada celda
columna_sin_texto = columna_datos.apply(lambda x: re.sub(r'\D', '', str(x)))

# Eliminar el signo '+' de cada celda
columna_sin_signo = columna_sin_texto.apply(lambda x: x.replace('+', ''))

# Eliminar espacios en blanco entre los números
columna_limpiada = columna_sin_signo.apply(lambda x: re.sub(r'\s', '', x))

# Crear un nuevo DataFrame con los números limpios
df_limpios = pd.DataFrame({'Numeros Limpios': columna_limpiada})

# Guardar los números limpios en un nuevo archivo Excel
df_limpios.to_excel(archivo_salida, index=False)








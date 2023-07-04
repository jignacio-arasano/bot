import pandas as pd
import re

# Ruta del archivo de entrada
archivo_entrada = 'dimaria7.xlsx'

# Ruta del archivo de salida
archivo_salida = 'dimaria777.xlsx'

# Columna a limpiar (indexada en base 0)
columna_limpiar = 0

# Leer archivo de entrada
df = pd.read_excel(archivo_entrada)

# Obtener los datos de la columna a limpiar
columna_datos = df.iloc[:, columna_limpiar]

# Función para extraer el número de teléfono
def extraer_numero_telefono(texto):
    patron = r'\+?\d+[\s\d-]*'
    numeros = re.findall(patron, str(texto))
    return numeros[0] if numeros else None

# Aplicar la función a cada celda de la columna
columna_numeros = columna_datos.apply(extraer_numero_telefono)

# Eliminar caracteres no numéricos de los números de teléfono
columna_numeros = columna_numeros.str.replace(r'\D', '')

# Crear un nuevo DataFrame con los números limpios
df_numeros = pd.DataFrame({'Número de Teléfono': columna_numeros})

# Guardar los números limpios en un nuevo archivo Excel
df_numeros.to_excel(archivo_salida, index=False)













import pandas as pd

# Cargar el archivo CSV
file_path = 'Productsex4.csv'
data = pd.read_csv(file_path)

# Eliminar la columna duplicada 'rank.1'
data = data.drop(columns=['rank.1'])

# Guardar los cambios en el mismo archivo o en uno nuevo
data.to_csv(file_path, index=False)  # Si quieres sobreescribir el archivo
# data.to_csv('ruta_del_archivo_limpio.csv', index=False)  # Si prefieres crear un nuevo archivo
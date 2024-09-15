'''
Ejercicio 2: Calcular el valor total del inventario y agregarlo al archivo original

Modifica el archivo original products.csv para añadir una columna llamada inventory_value, calculada como price * quantity. Luego, crea un nuevo archivo inventory_summary.csv que muestre el valor total del inventario y el número de productos en stock.

Objetivo:

	1.	Modificar el archivo original para añadir inventory_value.
	2.	Crear un archivo resumen con el valor total del inventario y cantidad de productos en stock.
'''

import csv, os
os.system('clear')

path = 'Productsex4.csv'
path2 = 'inventory_summary.csv'
total_value = 0
in_stock = 0

with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Solo añadimos 'inventory_value' si no existe ya en el archivo
    header = csv_reader.fieldnames
    if 'inventory_value' not in header:
        header = header + ['inventory_value']
    rows = []
    
    for row in csv_reader:
        # Si 'inventory_value' no existe, lo calculamos
        if 'inventory_value' not in row:
            row['inventory_value'] = float(row['price']) * float(row['quantity'])
        rows.append(row)

    fieldnames = ['total_value', 'in_stock']
        
    with open(path2, mode='w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames= fieldnames)
        csv_writer.writeheader()

        for row in rows:
            total_value += float(row['inventory_value']) #Se cambió de 'price' a 'inventory_value' ya que el ejercicio pide la sumatoria del valor total del inventario de cada producto. Corrección de chatGPT
            in_stock += float(row['quantity'])
        summary = {'total_value': total_value, 'in_stock': in_stock}
        csv_writer.writerow(summary)
    
    with open(path, mode='w', newline='') as newFile:
        csv_writer = csv.DictWriter(newFile, fieldnames= header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)

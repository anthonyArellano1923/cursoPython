'''
Ejercicio 3: Identificar productos de baja demanda y crear un archivo de ofertas

Modifica el archivo original products.csv añadiendo una columna llamada low_demand que indique yes si el producto tiene menos de 5 ventas (se puede asumir que el campo quantity indica las ventas) y no en caso contrario. Luego, crea un archivo discounted_products.csv con aquellos productos que tienen low_demand = yes y aplica un descuento del 20% sobre el precio.

Objetivo:

	1.	Modificar el archivo original para marcar los productos de baja demanda.
	2.	Crear un archivo con los productos de baja demanda y aplicarles un descuento.
'''
import csv, os, copy
os.system('clear')

path = 'Productsex4.csv'
lowDemandFile = 'discounted_products.csv'
low_demand = []
overwrite_file_rows = []

with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    header = csv_reader.fieldnames + ['low_demand']

    for row in csv_reader:
        if float(row['quantity']) < 5:
            row['low_demand'] = 'yes'
            print(row['price'], end=' ')
        else:
            row['low_demand'] = 'no'
        overwrite_file_rows.append(row)
        row_copy = copy.deepcopy(row)
        
        if float(row_copy['quantity']) < 5:
            row_copy['price'] = float(row_copy['price']) - float(row_copy['price']) * 0.2
            low_demand.append(row_copy)
            print(row_copy['price'])

    with open(lowDemandFile, mode='w', newline='') as discountedFile:
        csv_writer = csv.DictWriter(discountedFile, fieldnames= header)
        csv_writer.writeheader()
        csv_writer.writerows(low_demand)
    
    with open(path, mode='w', newline='') as overwrite:
        csv_writer = csv.DictWriter(overwrite, fieldnames= header)
        csv_writer.writeheader()
        csv_writer.writerows(overwrite_file_rows)

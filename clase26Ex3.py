'''Objetivo:

	1.	Añadir una columna rank al archivo original products.csv.
	2.	Crear un archivo con los 5 productos más caros.'''
'''import csv, os
os.system('clear')

def addToRanking(row):
    if len(rankingRows) < 5:
        rankingRows.append(row)
    return

path = 'Productsex4.csv'
path2 = 'ranking.csv'
rows = []
rankingRows = []

with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    header = csv_reader.fieldnames + ['rank']
    prices = [int(row['price']) for row in data]
    deltaPrices = max(prices) - min(prices)
    print(deltaPrices)
    rank5 = []
    rank4 = []
    rank3 = []
    rank2 = []
    rank1 = []

    for row in data:
        if int(row['price']) > deltaPrices*(4/5):
            row['rank'] = 5
            rank5.append(row)
            addToRanking(row)
        elif int(row['price']) > deltaPrices*(3/5):
            row['rank'] = 4
            rank4.append(row)
            addToRanking(row)
        elif int(row['price']) > deltaPrices*(2/5):
            row['rank'] = 3
            rank3.append(row)
            addToRanking(row)
        elif int(row['price']) > deltaPrices*(1/5):
            row['rank'] = 2
            rank2.append(row)
            addToRanking(row)
        else:
            row['rank'] = 1
            rank1.append(row)
        rows.append(row)


    with open(path2, mode='w', newline='') as new:
        csv_writer = csv.DictWriter(new, fieldnames= header)
        csv_writer.writeheader()
        csv_writer.writerows(rankingRows)

    with open(path, mode='w', newline='') as overwrite:
        csv_writer = csv.DictWriter(overwrite, fieldnames= header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)'''

import csv, os
os.system('clear')

def addToRanking(row):
    if len(rankingRows) < 5:
        rankingRows.append(row)

# Ruta del archivo original y el archivo para guardar el ranking
path = 'Productsex4.csv'
path2 = 'ranking.csv'
rows = []  # Aquí almacenaremos todos los productos con su nuevo rango
rankingRows = []  # Aquí almacenaremos solo los 5 productos más caros

with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)  # Convertimos el contenido del archivo en una lista de diccionarios
    header = csv_reader.fieldnames + ['rank']  # Añadimos la columna 'rank' al encabezado

    # Ordenamos los productos por precio de mayor a menor
    data.sort(key=lambda x: float(x['price']), reverse=True)

    # Asignamos rangos y añadimos los productos al nuevo archivo
    for index, row in enumerate(data):
        if index < 5:
            row['rank'] = 5
            addToRanking(row)  # Añadimos los 5 más caros a la lista rankingRows
        elif index < 10:
            row['rank'] = 4
        elif index < 15:
            row['rank'] = 3
        elif index < 20:
            row['rank'] = 2
        else:
            row['rank'] = 1
        rows.append(row)

    # Guardamos los 5 productos más caros en un archivo separado
    with open(path2, mode='w', newline='') as new:
        csv_writer = csv.DictWriter(new, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rankingRows)

    # Sobrescribimos el archivo original con los rangos asignados
    with open(path, mode='w', newline='') as overwrite:
        csv_writer = csv.DictWriter(overwrite, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)

import csv, os
os.system('clear')

#Leer archivo

'''with open('products.csv',  mode='r') as file:
    productsDict = csv.DictReader(file)
    for row in productsDict:
        print(row)'''

#Mostrar info por columnas.

'''with open('products.csv',  mode='r') as file:
    productsDict = csv.DictReader(file)
    for row in productsDict:
        print(f"Producto: {row['name']}, Marca: {row['brand']}, Precio: {row['price']}")'''

#Añadir infomarción al final de la tabla

'''new_product = {
    "name" : "Wireless Charger",
    "price" : 75,
    "quantity" : 100,
    "brand" : "ChargerMaster", 
    "category" : "Accessories",
    "entry_date" : "2024-07-01"
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)'''

#Crear archivo nuevo y columna con información adicional

originalFilePath = 'products.csv'
newFilePath = 'products_updated.csv'

with open(originalFilePath, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_value'] #Obtiene claves de archivo original y añade una nueva: 'total_value'

    with open(newFilePath, mode='w', newline='') as newFile:
        csv_writer = csv.DictWriter(newFile, fieldnames= fieldnames) #Crea la instancia de la clase Writer esta vez usando como nombres de campos la lista creada en base a las claves obtenidas del archivo leído.
        csv_writer.writeheader() #Escribe el encabezado.

        for row in csv_reader:
            row['total_value'] = float(int(row['price']) * int(row['quantity']))
            csv_writer.writerow(row)

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

new_product = {
    "name" : "Wireless Charger",
    "price" : 75,
    "quantity" : 100,
    "brand" : "ChargerMaster", 
    "category" : "Accessories",
    "entry_date" : "2024-07-01"
}

with open('products.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)
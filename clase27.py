import json, os
os.system('clear')

#Leer archivo

with open('products.json', mode='r') as file:
    products = json.load(file)

for item in products:
    print(f"Producto: {item['name']}, precio: {item['price']}")

#Añadir información

new_product = {
    "name": "Smartwatch",
    "price": 250,
    "quantity": 60,
    "brand": "TechTime",
    "category": "Wearables",
    "entry_date": "2024-08-15"
}

with open('products.json', mode='r') as file:
    products = json.load(file)
    products.append(new_product)

with open('products.json', mode='w') as file:
    json.dump(products, file, indent=3)
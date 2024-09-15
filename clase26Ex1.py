import os, csv
os.system('clear')

originalFile = 'products.csv'
newFile = 'products with discount.csv'
discount = 10 /100

with open(originalFile, mode='r') as file:
    nombrePico1 = csv.DictReader(file)
    header1 = nombrePico1.fieldnames + ['with_discount']

    with open(newFile, mode='w', newline='') as newArchive:
        nombrePico2 = csv.DictWriter(newArchive, fieldnames= header1)
        nombrePico2.writeheader()

        for nombrePico3 in nombrePico1:
            price = int(nombrePico3['price'])
            nombrePico3['with_discount'] = float(price - price * discount)
            nombrePico2.writerow(nombrePico3)
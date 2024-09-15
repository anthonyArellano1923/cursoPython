'''import os, csv
os.system('clear')

originalFile = 'products.csv'
reStockFile = 'reStock.csv'

with open(originalFile, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fileHeader = csv_reader.fieldnames + ['restock_needed']

    with open(reStockFile, mode='w', newline='') as newFile:
        csv_writer = csv.DictWriter(newFile, fieldnames= fileHeader)
        csv_writer.writeheader()

        for row in csv_reader:
            if int(row['quantity'] ) < 10: 
                row['restock_needed'] = 'yes' 
            else:
                row['restock_needed'] = 'no' 
            csv_writer.writerow(row) '''

import os, csv
os.system('clear')

originalFile = 'products.csv'
reStockFile = 'reStock.csv'

with open(originalFile, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fileHeader = csv_reader.fieldnames + ['restock_needed']

    with open(reStockFile, mode='w', newline='') as newFile:
        csv_writer = csv.DictWriter(newFile, fieldnames= fileHeader)
        csv_writer.writeheader()

        for row in csv_reader:
            if int(row['quantity'] ) < 10: 
                row['restock_needed'] = 'yes'
                csv_writer.writerow(row) 
            else:
                pass
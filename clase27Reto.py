import csv, json

path = 'products.json'
newCSV = 'clase27JSONtoCSV.csv'
keys = []

with open(path, mode='r') as file:
    jsonInfo = json.load(file)

    keys = list(jsonInfo[0].keys())
    
    with open(newCSV, mode='w', newline='') as newFile:
        csv_writer = csv.DictWriter(newFile, fieldnames= keys)
        csv_writer.writeheader()
        csv_writer.writerows(jsonInfo)

'''
Ejercicio 4: Convertir un archivo JSON a CSV

Usando el archivo JSON de usuarios, escribe un script que convierta los datos del archivo JSON a un archivo CSV. El archivo CSV debe tener las columnas nombre, edad, y correo electrónico.

Objetivos:

	•	Leer un archivo JSON.
	•	Crear y escribir un archivo CSV a partir de los datos JSON.
'''

import csv, json

path = 'clase27PracticeUsers.json'
newCSV = 'clase27Ex4CSV.csv'
fieldnames = ['Nombre', 'Edad', 'Email']
try:
	with open(path, mode='r') as file:
		jsonInfo = json.load(file)

		
		with open(newCSV, mode='w', newline='') as newFile:
			csv_writer = csv.DictWriter(newFile, fieldnames= fieldnames)
			csv_writer.writeheader()

			for person in jsonInfo:
				csv_writer.writerow({
						'Nombre': person.get('Nombre', 'N/A'),
						'Edad': person.get('Edad', 'N/A'),
						'Email': person.get('Email', 'N/A')
					})

			
except FileNotFoundError:
    print(f'Error: archivo {path} no encontrado en la ruta especificada.')
except json.JSONDecodeError:
    print(f"Error: archivo {path} no es un JSON válido.")
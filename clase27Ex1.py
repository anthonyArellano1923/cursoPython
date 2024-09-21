'''
Ejercicio 1: Leer y mostrar datos de un archivo JSON

Crea un archivo JSON con información de diferentes usuarios (nombre, edad, correo electrónico). El objetivo es escribir un script que lea el archivo y muestre en pantalla los datos de cada usuario con el siguiente formato:

Objetivos:

	•	Leer un archivo JSON.
	•	Iterar sobre una lista de diccionarios y mostrar los valores de las claves.
'''

import json

path = 'clase27PracticeUsers.json'

try:
    with open(path, mode='r') as file:
        data = json.load(file)
        
        for person in data:
            print(f"User: {person['Nombre']}, Age: {person['Edad']}, Email: {person['Email']}")
            
except FileNotFoundError:
    print(f'Error: archivo {path} no encontrado en la ruta especificada.')
except json.JSONDecodeError:
    print(f"Error: archivo {path} no es un JSON válido.")
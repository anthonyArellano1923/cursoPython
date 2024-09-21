'''
Ejercicio 3: Filtrar datos de un archivo JSON

Con el archivo JSON de usuarios creado anteriormente, escribe un script que lea el archivo y muestre únicamente los usuarios mayores de 30 años.

Objetivos:

	•	Leer y filtrar datos de un archivo JSON con base en una condición.
	•	Mostrar en pantalla solo los usuarios que cumplen con la condición.
'''

import json, os
os.system('clear')

path = 'clase27PracticeUsers.json'

try:
    with open(path, mode='r') as file:
        data = json.load(file)
        
        for person in data:
            if int(person['Edad']) > 30:
                print(f"Nombre: {person['Nombre']}, Edad: {person['Edad']}, email: {person['Email']}")
except FileNotFoundError:
    print(f'Error: archivo {path} no encontrado en la ruta especificada.')
except json.JSONDecodeError:
    print(f"Error: archivo {path} no es un JSON válido.")
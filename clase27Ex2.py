'''
Ejercicio 2: Agregar nuevos datos a un archivo JSON

A partir del archivo JSON creado en el ejercicio anterior, escribe un script que permita agregar un nuevo usuario al archivo. El usuario debe introducir el nombre, la edad y el correo electrónico del nuevo registro.

Objetivos:

	•	Leer el archivo JSON.
	•	Añadir nuevos datos proporcionados por el usuario.
	•	Guardar nuevamente los datos en el archivo JSON.

'''

import json, os
os.system('clear')

def getNameAndEmail():
    name = input('Introduzca nombre de usuario: ')
    email = input('Introduzca email de usuario: ')
    return name, email

def getAge():
    try:
        userAge = int(input('Introduzca edad de usuario: '))
        return userAge
    
    except ValueError:
        print('Introduce un número válido')
        return getAge()
          

path = 'clase27PracticeUsers.json'
name, email = getNameAndEmail()
age = getAge()


new_entry = {
      "Nombre": name,
      "Edad": age,
      "Email": email
    }

try:
    with open(path, mode='r') as file:
        data = json.load(file)
        user_exists = any(person['Email'].lower() == email.lower() for person in data)
        if not user_exists:
            data.append(new_entry)

            with open(path, mode='w') as newFile:
                json.dump(data, newFile, indent=3)
            print(f"Usuario {name} agregado exitosamente.")
        else:
            print(f"Usuario ingresado ya se encuentra en la base de datos.")
except FileNotFoundError:
    print(f'Error: archivo {path} no encontrado en la ruta especificada.')
except json.JSONDecodeError:
    print(f"Error: archivo {path} no es un JSON válido.")
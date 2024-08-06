import os
import random 

#Parte 1: if.
os.system('clear')

x1 = 5
y1 = 11 

if x1 > 10:
    print("Variable mayor a 10")
elif x1 == 10:
    print("Variable igual a 10")
else:
    print("Variable menor a 10")

#Parte 2: palabras reservadas

if x1 > 5 and y1 > 10:
    print("Condición 1 alcanzada")
elif x1 < 5 and y1 > 10:
    print("Condición 2 alcanzada")
elif x1 == 5 or y1 == 10:
    print("Condición 3 alcanzada")

#Parte 3: verificación true-false

library_members = { 
    'member1': {
        'Name': 'David Jones',
        'Gender': 'male',
        'Age': 25, 
        'Membership': False
        },
    'member2': {
        'Name': 'Linda Thomas', 
        'Gender': 'female', 
        'Age': 33, 
        'Membership': True
        },
    'member3':{
            'Name': 'Michael Smith', 
            'Gender': 'male', 
            'Age': 13, 
            'Membership': False
        },
    'member4': {
            'Name': 'Patricia Taylor', 
            'Gender': 'female', 
            'Age': 5, 
            'Membership': True
        },
    'member5': {
            'Name': 'John Doe', 
            'Gender': 'male', 
            'Age': 61, 
            'Membership': False
        },
    'member6': {
            'Name': 'John Aquaviva', 
            'Gender': 'male', 
            'Age': 18, 
            'Membership': True
        },
    'member7': {
            'Name': 'Lilian Tintori', 
            'Gender': 'male', 
            'Age': 14, 
            'Membership': False
        }    
    }

'''for members in library_members.values():
    print()
    for data, description in members.items():
        print(f'{data}: {description}')'''

for members in library_members.values():
    print()
    if members['Membership']:
        if members['Age'] >= 18:
            print(f"Miembro {members['Name']} admitido.")
        else:
            print(f"{members['Name']} es miembro pero tiene restricción de contenido por edad.")
    else:
        print(f"{members['Name']} no es un miembro de la biblioteca")
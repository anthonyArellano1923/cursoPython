def blanckspace():
    a = 0
    while a < 4:
        print()
        a += 1

worker = { 'name':'Anthony', 'position':'tecnitian', 'age': 30}
print('Worker\'s name', worker['name'])
print(worker)
del worker['age']
print(worker)

#Métodos
blanckspace()

contact = {
    'Name': 'Carla',
    'LastName': 'Quiñones',
    'Age': 30,
    'Stature': 1.60
}
print(contact)
keys = [value for value in contact.keys()]
values = [value for value in contact.values()]
items = [value for value in contact.items()]
print('Claves', keys,'Valores', values, 'Objetos', items, sep='\n')

#Diccionario de diccionarios

contacts = {
    'Ana' : {
        'LastName': 'Gonzalez',
        'Age': 30,
        'Height': 1.65,
        'Gender': 'Female'
    },
    'Pedro' : {
        'LastName': 'Perez',
        'Age': 34,
        'Height': 1.82,
        'Gender': 'Male'
    },
    'Carmen' : {
        'LastName': 'Torres',
        'Age': 22,
        'Height': 1.55,
        'Gender': 'Female'
    },
    'Jose' : {
        'LastName': 'Linarez',
        'Age': 27,
        'Height': 1.75,
        'Gender': 'Male'
    }
}
blanckspace()

for name in contacts:
    print(name)

blanckspace()

for name in contacts:
    print(f'Contact: {name}')
    for key, value in contacts[name].items():
        print(f'  {key}: {value}')
    print()

'''Esta es una manera diferente de hacerlo

for name, details in contacts.items(): // El método .items() devuelve un par clave:valor, estos se asignan a las variables name:details respectivamnte.
    print(f'Contact: {name}')
    for key, value in details.items(): // La variable details en si misma es otro diccionario así que se aplica la misma lógica del ciclo for anterior.
        print(f'  {key}: {value}')
    print()'''

#for person in contacts:
#    print(person.keys(), person.items(), sep='\n')

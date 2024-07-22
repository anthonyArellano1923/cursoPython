import ast
import random
import os

os.system('cls')

question1 = 'Desea eliminar elementos de la lista? [s/n]: '
question2 = 'Selecciona una opción del menú si: \n [a] Desea eliminar un elemento específico de la lista \n [b] Desea eliminar un rango de elementos de la lista \n [c] Desea eliminar todos los elementos de la lista \n [d] Salir \n'


'''def get_answer():
    user = input('Desea eliminar un elemento específico de la lista? [s/n]: ')
    if user == 's':
        return user
    elif user == 'n':
        return user
    else:
        print('Response solo son s (para si) n (para no)')
        get_answer()'''



def get_answer(menuQuestion):
    while True:
        user = input(menuQuestion)
        if user == 's' or user == 'n' or user == 'a' or user == 'b' or user == 'c' or user == 'd':
            return user
        else:
            if menuQuestion == question1:
                options = '[s] para si o [n] para no.'
            else:
                options = '[a], [b], [c] o [d]'
            print(f'Introduzca una opción válida: {options}')
    

def get_Index():
    while True:
        try:
            limit = len(random_list) - 1
            index = int(input('Ingrese el ídice deseado entre 0 y {}: '.format(limit)))
            if 0 <= index <= limit:
                return index
            else:
                print('ingrese un número dentro del rango válido')
        except ValueError:
            print('Ingrese solo números')


def getValue():
    user_input = input('Ingrese un elemento para buscar en la lista: ')
    try:
        value = ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        value = user_input
    element_type = type(value)
    return value, element_type


def deleteOneElement(): 
    index1 = get_Index()
    print(f'Eliminando {index1} de la lista')
    del random_list[index1]
    print('Quedan {} elementos en la lista'.format(len(random_list)))

#Listas!
lista_variedad = [42, 'Hola', 3.14, True, [1, 2, 3], {'nombre': 'Anthony', 'edad': 30}, (5, 6, 7), None, b'bytes', complex(2, 3)]
# .append .insert .index
print('Longitud de lista: ', len(lista_variedad),)

lista_variedad.append('Lilium, Elfen Lied')
print('Longitud de lista: ',len(lista_variedad), 'Posición 6 de la lista:', lista_variedad[6])

lista_variedad.insert(6, 'Se viene diccionario')
print('Longitud de lista: ', len(lista_variedad), 'Posición 6 de la lista:', lista_variedad[6])


'''list_element, element_type = getValue()
try: 
    print('El elemento ingresado es un tipo de datos:', element_type, '. Este se encuentra en la posición: ', lista_variedad.index(list_element))

except ValueError:
    print('El elemento ingresado es un tipo de datos:', element_type, 'y no está en la lista.')'''

# .min .max .del[n] .del[start:end:step]

random_list = [random.randint(1, 1000) for _ in range(50)]
for element in random_list:    
    print(element)
print('Elemento mayor:', max(random_list), 'Elemento menor:', min(random_list))

while True:
    question = get_answer(question1)
    if question == 's':
        question3 = get_answer(question2)
        if question3 == 'a' or question3 == 'b' or question3 == 'c':
            print(f'Seleccionaste opción: {question3}')
        else:
            print('Terminando.')
            break
        '''index1 = get_Index()
        print(index1, type(index1))
        del random_list[index1]
        print('Quedan {} elementos en la lista'.format(len(random_list)))'''
    else: 
        break
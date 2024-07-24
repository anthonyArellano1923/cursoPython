import ast
import random
import os

os.system('cls')

question1 = 'Desea manipular los elementos de la lista [s/n]: '
question2 = 'Selecciona una opción del menú si: \n [a] Desea eliminar un elemento específico de la lista \n [b] Desea eliminar un rango de elementos de la lista \n [c] Desea eliminar todos los elementos de la lista \n [d] Imprimir lista \n [e] Salir. \n '

def menu(random_list):
    print(' ')
    question3 = get_answer(question2)
    if question3 == 'a' or question3 == 'b' or question3 == 'c' or question3 == 'd':
        if question3 == 'a':
            if len(random_list) > 0:
                deleteOneElement()
            else:
                print('Lista vacía.')
                return
        elif question3 == 'b':
            if len(random_list) > 1:
                deleteRangeOfElements()
            else:
                print('No es posible eliminar un rango de elementos si la lista contiene menos de 2 elementos.')
                return
        elif question3 == 'c':
            if len(random_list) > 0:
                del random_list
                print('Lista eliminada')
            else:
                print('La lista ya está vacía')
                return
        elif question3 == 'd':
            print(random_list)     
    else:
        print('Terminando.')            
        return


def get_answer(menuQuestion):
    while True:
        user = input(menuQuestion)
        if user == 's' or user == 'n' or user == 'a' or user == 'b' or user == 'c' or user == 'd' or user == 'e':
            return user
        else:
            if menuQuestion == question1:
                options = '[s] para si o [n] para no.'
            else:
                options = '[a], [b], [c] o [d]'
            print(f'Introduzca una opción válida: {options}')
    
def addElement():
    value = getValue()
    random_list.append(value)
    return
    


def get_Index():
    while True:
        try:
            limit = len(random_list) - 1
            index = int(input('Ingrese el ídice deseado entre 0 y {}: '.format(limit)))
            if 0 <= index <= limit:
                return index
            else:
                print('ingrese un número dentro del rango válido')
                return get_Index()
        except ValueError:
            print('Ingrese solo números')


def get_IndexRange1():
    while True:
        try:
            limit = len(random_list) - 2 #El índice inicial debe estar entre el primer y el penúltimo elemento de la lista.
            index = int(input('Ingrese el ídice deseado entre 0 y {}: '.format(limit)))
            if 0 <= index <= limit:
                return index
            else:
                print('Ingrese un número dentro del rango válido')
                return get_IndexRange1()
        except ValueError:
            print('Ingrese solo números')


def get_IndexRange2(indexR1, lastIndex):
    while True:
        try:
            index = int(input(f'Ingrese un índice entre {indexR1} y {lastIndex}: '))
            if indexR1 < index <= lastIndex:
                return index
            else:
                print('Ingrese un índice que esté dentro del rango seleccionado')
                return get_IndexRange2(indexR1, lastIndex)
        except ValueError:
            print('Ingrese solo números')


def getValue():
    user_input = input('Ingrese un elemento para añadir a la lista: ')
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


def deleteRangeOfElements():
    indexR1 = get_IndexRange1()
    lastIndex = len(random_list) - 1
    indexR2 = get_IndexRange2(indexR1, lastIndex)
    del random_list[indexR1:indexR2]
    print(f'Se eliminaron los elementos entre los índices {indexR1} y {indexR2}. Quedan {len(random_list)} elementos.')


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
    print(' ')
    question = get_answer(question1)
    if question == 's':
        menu(random_list)
    elif question == 'n':
        print('Terminado')
        break
    else: 
        print('Introduzca una respuesta válida: [s] para si, [n] para no.')
    
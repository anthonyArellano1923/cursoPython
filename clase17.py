#Funciones
def greet(name='Sin Nombre', lastName='Sin apellido'):
    print('Hola', name, lastName)
    return

name_list = ['Carla', 'Jose']
lastName_list = ['Sequera', 'Rodriguez']

greet(name_list[0], lastName_list[0])
greet(name_list[1], lastName_list[1])
greet(lastName = lastName_list[0])
greet(name = name_list[1])
greet()

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def get_num(mensaje):
    try:
        num = int(input(mensaje))
        return num
    except ValueError:
        print('Ingrese un número válido')
        get_num(mensaje)

def get_option():
    option = input('Ingrese una opción: ')
    if option in ['1','2','3','4','5']:
        return option
    else:
        print('Ingrese una opción válida.')
        print()
        get_option()

def print_menu():
    print('Seleccione una opción:')
    print('1.Suma', '2.Resta', '3.Multiplicación', '4.División', '5.Salir', sep='\n')

while True:
    print()
    print('Calculdora simple')
    print_menu()
    option = get_option()
    if option == '5':
        break
    num1 = get_num('Ingrese primer dígito: ')
    num2 = get_num('Ingrese segundo dígito: ')
    print()
    if option == '1':
        print('Suma = ', num1 + num2)
    elif option == '2':
        print('Resta = ', num1 - num2)
    elif option == '3':
        print('Mutiplicación = ', num1 * num2)
    elif option == '4':
        if num2 != 0:
            print('Resta = ', num1 / num2)
        else:
            print('No se admiten divisiones entre 0')
    

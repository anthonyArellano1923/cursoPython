def get_valid_int(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Introduzca número válido')


persona = {
    "name" : input('Introduzca primer nombre: '),
    "lastName" : input('Introduzca apellido paterno: '),
    "age" : get_valid_int('Introduzca edad: '), 
    "phoneNumber" : get_valid_int('Introduzca número de teléfono: ')
}

print(f'Usuario 1: \n Nombre completo: {persona["name"]} {persona["lastName"]} \n Edad: {persona["age"]} \n Número de Teléfono: {persona["phoneNumber"]}')
print('La edad es un: ', type(persona["age"]))
print('El número de teléfono es un: ', type(persona["phoneNumber"]))

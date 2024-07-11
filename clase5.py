variables = ['str', 1, 1.2]
for element in variables:
    print(type(element), element)
cadena = 'Mamame el webo menor'
counter = len(cadena)
while counter != 0:
    print(cadena[-(len(cadena)+1)+counter])
    counter -= 1

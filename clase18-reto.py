#Crear un filtro de letras para un texto introducido.
import string
import os
os.system('clear')

'''paragraph = input('Contador de vocales, consonantes y palabra especial. \n Introduce un texto:\n')
specialWord = input('¿Qué palabra deseas contar?: \n')
vocalsInText = list(filter(lambda x: x in 'aeiouáéíóú', paragraph.lower()))
consonantsInText = list(filter(lambda x: x in string.ascii_letters and x not in 'aeiouáéíóú', paragraph.lower()))
SIsInText = list(filter(lambda x: x == specialWord, paragraph.lower().split()))
print('Cantidad de vocales:', len(vocalsInText))
print('Cantidad de consonantes:', len(consonantsInText))
print(f'Cantidad de veces que aparece la palabra [{specialWord}]:', len(SIsInText))'''

#Función que devuelva las mayúsculas de una cadena de texto

'''lowerString = 'Hola, vengo de tangamandapio.'
upperString = ''.join(list(map(lambda x: x.upper(), lowerString)))
print(upperString)'''

#Funcion que guarde solo palabras de más de 5 caracteres

'''paragraph = 'El viento susurraba entre las hojas de los árboles, llevando consigo el aroma de la tierra húmeda tras la lluvia. Los pájaros cantaban melodías suaves, creando una sinfonía natural que se mezclaba con el murmullo del río cercano. Cada gota de agua reflejaba un fragmento de cielo, mientras los rayos de sol jugaban a través de las nubes dispersas. La paz reinaba en este rincón escondido del mundo, donde el tiempo parecía detenerse y la naturaleza mostraba su esplendor en cada rincón.'
only_letters = ''.join(list(filter(lambda x: x in string.ascii_letters or x == ' ' or x in 'áéíúóü', paragraph.lower())))
print(list(filter(lambda x: len(x) > 5, only_letters.split())))'''

#Suma de dígitos.

list1 = [345, 678, 1234]
'''list2 = []

for number in list1:
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    list2.append(digit_sum)

print(list2)'''

list2 = [str(element) for element in list1]
print(list2)
result = list(map(lambda x: sum(int(digit) for digit in x), list2))
print(result)



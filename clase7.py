import math

#Impresión de mensaje simple.
print('Hola mundo')

#Uso de comillas
print('''Hola mundo, cómo estás?
Esto es un mensaje con
distintos saltos de línea.
Bienvenido al print multilínea''')

#Usos de la coma
print('Platzi', 'nunca', 'pares', 'de', 'aprender')

#Concatenación
print('Platzi' + 'nunca' + 'pares' + 'de' + 'aprender')

#Uso de sep=''
print('Platzi', 'nunca', 'pares', 'de', 'aprender', sep=", ")
print('Platzi', 'nunca', 'pares', 'de', 'aprender', sep="\n")
print('Platzi', 'nunca', 'pares', 'de', 'aprender', sep=" ")
print('Platzi', 'nunca', 'pares', 'de', 'aprender', sep="?")

#Usos de end=''
print("Nunca", end=" ")
print("pares de aprender")
print("Nunca", end=".")
print("pares de aprender")
print("Nunca", end="&")
print("pares de aprender")

#Impresión de variables
frase = 'No me digas nada, no quiero escucarte'
autor = 'Binomio de oro'
print('Frase: ' + frase)
print('Autor: ' + autor)

#Uso de f-strings
print(f"Frase: {frase}, Autor: {autor}")

#Uso de .format()
print("Frase: {}, Autor: {}".format(frase, autor))

#mpresión con formato específico: {:.nf}

pi = math.pi
print("Valor de pi = {:.2f}".format(pi))
print("Valor de pi = {:.3f}".format(pi))
print("Valor de pi = {:.4f}".format(pi))
print("Valor de pi = {:.5f}".format(pi))

#Secuencias de escape y saltos de línea

print("Hola, acá \n saltos de línea con \n secuencias de escape!")
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

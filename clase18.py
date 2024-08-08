#Función lambda
add = lambda a, b: a + b
print('Suma:', add(10,4))

multiply = lambda a, b: a * b
print('Multiplicación:', multiply(10,4))

#Función Map

base_list = list(range(35))

quadruple_list = list(map(lambda x: x**2, base_list))

print(base_list, quadruple_list, sep='\n')

#Función filter

even = list(filter(lambda x: x%2 == 0, quadruple_list))
print(even)
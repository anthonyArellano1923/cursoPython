#Creando iterador
list2 = [1, 2, 3, 4]
iterator = iter(list2)

print(next(iterator))

print(next(iterator))

print(next(iterator))

print(next(iterator))

#print(next(iterator)) Prueba de stopIteration

#Iter a partir de str

text5 = "Kill for pleasure"

textIter = iter(text5)

for char in textIter:
    print(char)

textIter2 = iter(text5)

for char1 in range(len(text5)):
    print(next(textIter2))

#Iterador de números pares e impares
limit = 30
pares = iter(range(0, limit + 1, 2))
impares = iter(range(1, limit + 1, 2))
list_of_ip = [[],[]]

for num_p in pares:
    list_of_ip[0].append(num_p)
for num_i in impares:
    list_of_ip[1].append(num_i)

print(list_of_ip[0])
print(list_of_ip[1])

#Generador

def generator2():
    yield 1
    yield 2
    yield 3

for element in generator2():
    print(element)
for _ in range(100):
    print()
#fibonacci

def fiboCool(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for fiboNum in fiboCool(100):
    print(fiboNum)


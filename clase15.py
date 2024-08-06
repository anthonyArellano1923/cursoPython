#Bucle for
numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print('Acá está el valor actual de i:', i)

#Rango de elementos

for i in range(3,10):
    print(i)

#Condicional dentro del for.

fruits = ["Pera", "Manzana", "Tomate", "Naranja", "Limón", "Coco"]

for fruit in fruits:
    if fruit == "Naranja":
        print("Naranja encontrada")
    else:
        print(f"No es una naranja, es {fruit}")

#While

an = 0
while an < 5:
    print(an)
    an += 1

#Rompiendo While

an = 0
while an < 6:
    if an == 5:
        break
    print(an)
    an += 1

for o in numbers:
    if o == 4:
        continue
    print('Acá está el valor actual de o:', o)
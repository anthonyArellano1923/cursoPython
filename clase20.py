#Función recursiva: factorial

def factorial(index):
    if index > 0:
        return index * factorial(index-1)
    else:
        return 1

factorial_n = factorial(10)
print(factorial_n)

#Función recursiva: fibonacci

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_index = [fibonacci(index) for index in range(12)]
print(fibonacci_index)

#Reto: crea una función recursiva que sume los números naturales

def suma_natural(number):
    if number == 0:
        return number
    else:
        return number + suma_natural(number-1)

sumNumber = 15
print(suma_natural(sumNumber))
print([suma_natural(index) for index in range(sumNumber+1)])
import math

def simulate_data():
    for i  in range(1,1001):
        yield i

def evens(iterator):
    for num in iterator:
        if num % 2 == 0:
            yield num

def cuadratic(iterator):
    for i in iterator:
        yield i ** 2

evensFilter = cuadratic(evens(simulate_data()))

for number in evensFilter:
    print(number, int(number ** 0.5), sep='   ')
def gen_even():
    a = 0
    while True:
        yield a
        a += 2

def gen_odd():
    b = 1
    while True:
        yield b 
        b += 2

def multiples_generator(multiplier):
    c = 1
    while True:
       yield c * multiplier
       c += 1
       
limit = 20
multiplier = 10
even_generator = gen_even()
odd_generator = gen_odd()
multiplier_ngenerator = multiples_generator(multiplier)
list_of_evens = []
list_of_odds = []
list_of_multipliers = []


for _ in range(limit):
    list_of_evens.append(next(even_generator))
    list_of_odds.append(next(odd_generator))
    list_of_multipliers.append(next(multiplier_ngenerator))

print(list_of_multipliers, list_of_evens, list_of_odds, sep='\n')
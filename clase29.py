import os, math, random
os.system('clear')

#Librería OS

'''current_path = os.getcwd()
print('Directorio actual: ',current_path)'''


'''os.rename('ranking.csv', 'ranking2.csv')

archivos_csv = [archivo for archivo in os.listdir('.') if archivo.endswith('.csv')]

for element in archivos_csv:
    print(element)'''

#Librería Math

'''radius = 10
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(f"Para un círculo de radio {radius:.2f}, su área es: {area:.2f} y su perímetro: {perimeter:.2f}")'''

#librería Random

random_number = random.randint(1,10)
print(random_number)

random_colour = ['green', 'yellow', 'orange']
print(random.choice(random_colour))

cards = ['as', 'queen', 'king', '5', 'joker']
print(cards)
random.shuffle(cards)
print(cards)


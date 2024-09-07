'''with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())'''

'''with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)'''

'''with open('caperucita.txt', 'a') as file:
    for _ in range(5):
        file.write("\n \nPlus added.")'''

with open('caperucita.txt', 'w') as file:
    for _ in range(5):
        file.write("Su información se perdió.\n")

        
while (True):
    try:
        number_1 = int(input('Ingresa número A: '))
        number_2 = int(input('Ingresa número B: '))

        print('A * B = ', number_1 * number_2)
        print('A + B = ', number_1 + number_2)
        try:
            print('A / B = ', number_1 / number_2)
        except ZeroDivisionError: 
            print('A / B = X No es posible dividir entre 0')
        print('A - B = ', number_1 - number_2)
        
        print('A ^ B = ', number_1 ** number_2)
        try:
            print('Entero de A / B = ', number_1 // number_2)
        except ZeroDivisionError: 
            print('Entero de A / B = X No es posible dividir entre 0')
        try:
            print('Módulo de A / B = ', number_1 % number_2)
        except ZeroDivisionError: 
            print('Módulo de A / B = X No es posible dividir entre 0')

        print('A > B :', number_1 > number_2)
        print('A < B :', number_1 < number_2)
        print('A >= B :', number_1 >= number_2)
        print('A <= B :', number_1 <= number_2)
        print('A == B :', number_1 == number_2)
        print('A != B :', number_1 != number_2)
    except ValueError:
        print('Ingrese un número válido')
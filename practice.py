import os
os.system('clear')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter (self):
        return 2 * (self.height + self.width) 

    
    def showDimensions(self):
        return "Ancho = " + str(self.width) + " Altura = " +str(self.height)

rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(5, 10)

print(f"Datos de Rectángulo 1: \n  -Dimensiones: {rectangle1.showDimensions()} \n  -Área = {rectangle1.area()}\n  -Perímetro = {rectangle1.perimeter()}\n")
print(f"Datos de Rectángulo 2: \n  -Dimensiones: {rectangle2.showDimensions()} \n  -Área = {rectangle2.area()}\n  -Perímetro = {rectangle2.perimeter()}")
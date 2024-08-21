'''
Reto
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.
'''
import time
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.newState = True

    def showCarInfo(self):
        print("Modelo: {}\nPrecio: {:.2f}$".format(self.model, self.price))


class Client:
    def __init__(self, name, iD):
        self.name = name
        self.iD = iD
        self.ownedCars = [] 
    
    def clientBuyCar(self, car, dealership=None):
        if dealership == None:
            dealership = dealership1()
        if car in dealership.newCarsInStock or car in  dealership.usedCarsInStock:  #Verifica si el auto está en stock
            dealership.dealerSaleCar(car)                                           #Esta funcion elimina el auto de la lista de autos del consecionario. 
            self.ownedCars.append(car)
            print("Cliente {} ha comprado un {} por {:.2f}$".format(self.name, car.model, car.price))
            if car.newState == True:
                car.newState = False
            car.price *=0.90
        else:
            print("Auto no disponible en consecionario.") 

    def clientSaleCar(self, car, dealership=None):
        if dealership == None:
            dealership = dealership1()
        dealership.dealerBuyCar(car)
        self.ownedCars.remove(car)
        print("Cliente {} ha vendido su {} a concesionaria por {:.2f}$.".format(self.name, car.model, car.price))
        car.price *= 1.05

    def clientAvailibleCars(self):
        if len(self.ownedCars) > 0:
            print(f"Autos en posesión del cliente {self.name}: ")
            for car in self.ownedCars:
                print("   -{}, valorado en {:.2f}".format(car.model, car.price))
        else:
            print(f"Cliente {self.name} no posee ningún auto.")

    

class Dealership:
    def __init__(self):
        self.clients = []
        self.cars = []
        self.newCarsInStock = []
        self.usedCarsInStock = [] 
    
    def registerClient(self, client):
        clientsIds = []
        for clientIn in self.clients:
            clientsIds.append(clientIn.iD)  
        if client.iD not in clientsIds:
                self.clients.append(client)
                print(f"Cliente frecuente {client.name} con el ID {client.iD} registrado con éxito")
        else:
            print(f"Cliente {client.name} ya se encuantra en la base de datos bajo el ID {client.iD}")
        
    def registerCar(self, car):
        if car.newState:
            self.newCarsInStock.append(car)
            print(f"Auto {car.model} añadido con éxtito a stcok de autos nuevos")
        else:
            self.usedCarsInStock.append(car)
            print(f"Auto {car.model} añadido con éxtito a stcok de autos nuevos")

    def dealerSaleCar(self, car):
        if car in self.newCarsInStock and car.newState == True:
            self.newCarsInStock.remove(car)
        elif car in self.usedCarsInStock and car.newState == False:
            self.usedCarsInStock.remove(car)
        

    def dealerBuyCar(self, car):
        self.usedCarsInStock.append(car)

    def showAvailibleCars(self):
        print("Autos nuevos disponilbes:")
        if len(self.newCarsInStock) > 0:
            for car in self.newCarsInStock:
                print("   -{}, price {:.2f}$".format(car.model, car.price))
            print()
        else: 
            print("No hay autos nuevos disponibles.")
        if len(self.usedCarsInStock) > 0:
            print("Autos usados disponilbes:")
            for car in self.usedCarsInStock:
                print("   -{}, price {:.2f}$".format(car.model, car.price))
            print()
        else:
            print("No hay autos usados disponibles.")

'''dealership1 = Dealership()

car1 = Car('Model S', 79999)
car2 = Car('Model 3', 39999)
car3 = Car('Model X', 89999)
car4 = Car('Model Y', 49999)
car5 = Car('Cybertruck', 69999)

cars = [car1, car2, car3, car4, car5]

client1 =  Client('John Doe', 123456789)
client2 =  Client('Jane Smith', 987654321)
client3 =  Client('Alice Johnson', 567890123)
client4 =  Client('Bob Brown', 234567890)
client5 =  Client('Charlie Davis', 345678901)
client6 =  Client('Charlie Davis', 345678901)

clients = [client1, client2, client3, client4, client5, client6]

for car in cars:
    dealership1.registerCar(car)

for client in clients:
    dealership1.registerClient(client)

print()

dealership1.showAvailibleCars()

while car1.price > 60000:
    client1.clientBuyCar(car1,dealership1)
    print("{:.2f}".format(car1.price))
    client1.clientAvailibleCars()
    client1.clientSaleCar(car1,dealership1)
    print("{:.2f}".format(car1.price))
    dealership1.showAvailibleCars()
    time.sleep(0.5)

client2.clientBuyCar(car1, dealership1)
client2.clientBuyCar(car2, dealership1)
client2.clientBuyCar(car3, dealership1)
client2.clientBuyCar(car4, dealership1)
client2.clientBuyCar(car5, dealership1)

dealership1.showAvailibleCars()
print()
client2.clientAvailibleCars()

client2.clientSaleCar(car1, dealership1)
client2.clientSaleCar(car2, dealership1)
client2.clientSaleCar(car3, dealership1)
client2.clientSaleCar(car4, dealership1)
client2.clientSaleCar(car5, dealership1)

dealership1.showAvailibleCars()
print()
client2.clientAvailibleCars()'''









# clientX.buyCar(car, dealership=dealership1)
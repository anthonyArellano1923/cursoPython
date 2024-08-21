'''
Reto
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.
'''

class Car:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price
        self.stateNew = True
        self.availible = True
    
    def showCarInfo(self):
        print(f"-Modelo: {self.model} \n-Marca: {self.brand} \n-Precio: {self.price}")

class Client:
    def __init__(self, name, iD):
        self.name = name
        self.iD = iD
        self.carsOwned = []

    def buyCar(self, car):
        if car.availible == True:
            self.carsOwned.append(car)
            car.availible = False
            car.stateNew = False
            car.price *= 75/100
        else:
            print("Auto no disponible para la venta")

    def saleCar(self, car):
        if len(self.carsOwned) > 0:
            car.availible = True
            self.carsOwned.pop(car)
        else:
            print("No tienes autos disponibles para la venta")
    
    def registerUserCar(self, car):
        self.carsOwned.append(car)
        car.stateNew = False
        print("Auto agregado al haber del cliente") #Revisar caso de registrar 2 autos de la misma marca y vender 1.
    
    def showUsersCars(self):
        if len(self.carsOwned) > 0:
            print(f"El usuario {self.name} tiene en posesión:")
            for car in self.carsOwned:
                print(f"    -{car.model}")
        else:
            print(f"Cliente {self.name} no posee autos comprados")
    

class Dealership:
    def __init__(self):
        self.clients = []
        self.newCars = []
        self.usedCars = []

    def registerCar(self, car):
        print()
        if car.stateNew:
            self.newCars.append(car)
            print(f"Auto {car.model} añadido al stock de autos nuevos exitosamente.")
        else:
            self.newCars.append(car)
            print(f"Auto {car.model} añadido al stock de autos usados exitosamente.")
            print(self.newCars)
    
    def registerClient(self, client):
        clientsIds = []
        for iDs in self.clients: 
            clientsIds.append(iDs.iD)
        
        if client.iD not in clientsIds:
            self.clients.append(client)
            print(f"Cliente frecuente {client.name} con el ID {client.iD} registrado con éxito")
        else:
            print(f"Cliente ya se encuantra en la base de datos. (ID {client.iD})")
    
    def showAvailibleCars(self):
        print()
        if len(self.newCars) > 0 or len(self.usedCars) > 0 :
            print("Autos nuevos disponibles:")
            for car in self.newCars:
                print(f"    -{car.model}")
            print("Autos usados disponibles:")
            for car in self.usedCars:
                print(f"    -{car.model}")
    
    def deleteCar(self, car):
        if car.stateNew == True :
            self.newCars.pop(car)
        else:
            self.usedCars.pop(car)
        print(f"{car.model} ha sido sacado de stock por venta.")

    def addCar(self, car):
        if car.stateNew == True :
            self.newCars.append(car)
        else:
            self.usedCars.append(car)
        print(f"{car.model} ha sido ingreado al stock por compra.")
    
dealership1 = Dealership()

dealership1.showAvailibleCars()

client1 = Client("Ana Pérez", "001")
client2 = Client("Luis García", "002")
client3 = Client("Marta Fernández", "003")
client4 = Client("Javier Gómez", "004")
client5 = Client("Claudia Rodríguez", "005")

car1 = Car('Corolla', 'Toyota', 21000)
car2 = Car('Camry', 'Toyota', 27000)
car3 = Car('RAV4', 'Toyota', 30000)
car4 = Car('Highlander', 'Toyota', 36000)
car5 = Car('Land Cruiser', 'Toyota', 85000)

car6 = Car('Fiesta', 'Ford', 20000)
car7 = Car('Focus', 'Ford', 25000)
car8 = Car('Mustang', 'Ford', 43000)
car9 = Car('Explorer', 'Ford', 35000)
car10 = Car('F-150', 'Ford', 40000)

car11 = Car('3 Series', 'BMW', 42000)
car12 = Car('5 Series', 'BMW', 55000)
car13 = Car('X3', 'BMW', 50000)
car14 = Car('X5', 'BMW', 60000)
car15 = Car('7 Series', 'BMW', 90000)

car16 = Car('A3', 'Audi', 33000)
car17 = Car('A4', 'Audi', 39000)
car18 = Car('Q5', 'Audi', 45000)
car19 = Car('Q7', 'Audi', 55000)
car20 = Car('A8', 'Audi', 85000)

car21 = Car('A-Class', 'Mercedes-Benz', 34000)
car22 = Car('C-Class', 'Mercedes-Benz', 42000)
car23 = Car('E-Class', 'Mercedes-Benz', 55000)
car24 = Car('GLC', 'Mercedes-Benz', 50000)
car25 = Car('S-Class', 'Mercedes-Benz', 95000)

carsList = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14, car15, car16, car17, car18, car19, car20, car21, car22, car23, car24, car25]




clientsList = [client1, client2, client3, client4, client5]

for client in clientsList:
    dealership1.registerClient(client)

for car in carsList:
    dealership1.registerCar(car)

dealership1.showAvailibleCars() #Comprobar funcionamiento de métodos de compra y venta.

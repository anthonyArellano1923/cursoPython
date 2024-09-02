#Como el código de la clase no tiene mucho sentido para mi, tuve que inventarme un ejercicio
#con ayuda de chatGPT


'''
base: CuentaBancaria
	•	Atributos protegidos:
	•	_titular: Nombre del titular de la cuenta.
	•	_saldo: Saldo actual de la cuenta (inicializado en 0).
	•	_historial_transacciones: Lista que almacena el historial de transacciones realizadas (depósitos y retiros).
	•	Métodos públicos:
	•	depositar(cantidad): Recibe una cantidad y la añade al saldo de la cuenta. También registra la transacción en el historial.
	•	retirar(cantidad): Recibe una cantidad y la resta del saldo de la cuenta, si hay suficiente saldo. Si no hay suficiente saldo, muestra un mensaje indicando que la operación no es posible. También registra la transacción en el historial si es exitosa.
	•	mostrar_saldo(): Muestra el saldo actual de la cuenta.
	•	mostrar_historial(): Muestra el historial completo de transacciones.
	•	Métodos abstractos (se definirán en las subclases):
	•	aplicar_interes(): Método abstracto que debe ser implementado por cada subclase, ya que el cálculo del interés varía según el tipo de cuenta.
	2.	Subclase: CuentaCorriente
	•	Atributos adicionales:
	•	_limite_descubierto: Límite de dinero que puede retirar la cuenta por encima del saldo (descubierto).
	•	Métodos específicos:
	•	Sobrescribe el método retirar(cantidad) para permitir el descubierto hasta un límite especificado.
	•	Implementa el método aplicar_interes(), que no hace nada ya que las cuentas corrientes no generan intereses.
	3.	Subclase: CuentaAhorro
	•	Atributos adicionales:
	•	_tasa_interes: Tasa de interés anual de la cuenta de ahorro.
	•	Métodos específicos:
	•	Implementa el método aplicar_interes() para aplicar el interés al saldo basado en la tasa de interés.


'''
import os, random
os.system("clear")

class BankAccount:
    def __init__(self, accountHolder, balance):
        self.balance = balance
        self.accountHolder = accountHolder
        self.history = []
        self.comissions = 0

    
    def deposit(self, amount):
        if amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.")
            return 
        self.balance += amount
        self.history.append(f"Depósito recibido por {amount:.2f}")
        print(f"Depósito recibido en cuenta de cliente {self.accountHolder} por {amount}. Nuevo saldo actual: {self.balance:.2f}\n") 

    def withdraw(self, amount):
        if amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.")
            return 
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Retiro realizado por {amount:.2f}")
            print(f"Retiro realizado de cuenta de cliente {self.accountHolder} por {amount:.2f}. \nNuevo saldo actual: {self.balance:.2f}")
        else:
            print(f"Fondos insuficientes en la cuenta de cliente {self.accountHolder} para realizar el retiro deseado.")
            self.history.append(f"Operación rechazada por saldo insuficiente.")

    def transfer(self, amount, client):
        if self.balance < amount:
            print("Monto supera saldo actual.")
            return
        elif amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.")
            return
        client.balance += amount
        client.history.append(f"Transferencia recibida de cliente {self.accountHolder} por {amount:.2f}, Nuevo saldo actual: {client.balance:.2f}")
        self.balance -= amount
        self.history.append(f"Transferencia enviada a cliente {client.accountHolder} por {amount:.2f}")
        print(f"Transferecia enviada exitosamente a cliente {client.accountHolder} por {amount:.2f}.  \nNuevo saldo actual: {self.balance:.2f}\n")
    
    def showBalance(self):
        return print(f"Saldo actual de cliente {self.accountHolder}: {self.balance:.2f}\n")
    
    def showClientHistory(self):
        if len(self.history) > 0:
            print(f"Mostrando historial de cliente {self.accountHolder}:")
            for movement in self.history:
                print(f"  -{movement}")
            print()
        else:
            print(f"No hay movimientos en la cuenta de cliente {self.accountHolder} \n")

    def showComissions(self):
        print(f"El cliente {self.accountHolder} debe comisiones de operación por un total de {self.comissions:.2f}\n")

    def applyInterests(self):
        previousBalance = self.balance
        self.balance += self.balance * self.interests/100
        newBalance = self.balance
        self.history.append(f"Intereses aplicados del {self.interests:.2f}%, abonando {- previousBalance + newBalance:.2f} a la cuenta del cliente.")
        print(f"Aplicado intereses del {self.interests}%, nuevo saldo actual de cliente {self.accountHolder} : {self.balance:.2f}")

    def getBalance(self):
        return self.balance
    
    def getComissions(self):
        return self.comissions
    
    def payComissions(self, amount):
        if self.comissions <= 0:
            print(f"Cliente {self.accountHolder} no adeuda comisiones.")
            return
        
        if amount > self.comissions:
            print(f"Monto indicado supera el valor adeudado, intente con otro monto.\n")
            return
        elif amount <= 0:
            print(f"Monto indicado debe ser superior a cero, intente con otro monto.\n")
            return
        self.comissions -= amount
        self.history.append(f"Abono a comisiones por {amount:.2f}")
        if self.comissions > 0:
            print(f"Se han pagado {amount:.2f} como abono a tus comisiones. Restan {self.comissions:.2f}\n")
        else:
            print(f"Se han pagado {amount:.2f} como abono total a tus comisiones.\n")

    def showAvailableOverchage(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class CurrentAccount(BankAccount):
    def __init__(self, accountHolder, balance, overcharge=10000, maintenance=0.5):
        super().__init__(accountHolder, balance)
        self.overcharge = overcharge
        self.maintenance = maintenance

    def withdraw(self, amount):
        if amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.\n")
            return 
        
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Retiro realizado por {amount:.2f}")
            print(f"Retiro realizado de cuenta de cliente {self.accountHolder} por {amount:.2f}. \nNuevo saldo actual: {self.balance:.2f}, Sobregirio disponible: {self.overcharge:.2f} \n")
        elif self.balance + self.overcharge >= amount:
            self.balance -= amount
            self.comissions += self.overcharge * 1 /100
            self.history.append(f"Retiro realizado por {amount:.2f}")
            print(f"Retiro realizado de cuenta de cliente {self.accountHolder} por {amount:.2f}. \nNuevo saldo actual: {self.balance:.2f}, sobregiro disponible: {self.overcharge + self.balance:.2f}.")
            print(f"Se ha usado {self.overcharge - (self.overcharge + self.balance):.2f} de tu sobregiro.\n")                
        else: 
            print(f"Cantidad {amount:.2f} supera el monto disponible para retiro. Disponible para retirar: {self.overcharge + self.balance :.2f}")
            self.history.append(f"Operación rechazada por fondos insuficientes.")
        
    def applyInterests(self):
        self.history.append(f"Transacción inválida.")
        return print("La cuenta corriente no genera intereses.\n")
    
    
    def transfer(self, amount, client):
        if self.accountHolder == client.accountHolder and self.balance == client.balance:
            print(f"Cliente de destino es el mismo que el origen, intente con otro cliente.\n")
            return
        if amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.\n")
            return
        if client.accountHolder == self.accountHolder:
            print(f"Cliente no puede transferirse a si mismo, intente con un cliente distinto.\n")
            return
        
        if self.balance >= amount:
            super().transfer(amount, client)
        elif self.balance + self.overcharge >= amount:
            self.balance -= amount
            client.balance += amount
            self.comissions += self.overcharge * 1 /100
            client.history.append(f"Transferencia recibida de cliente {self.accountHolder} por {amount:.2f}, Nuevo saldo actual: {client.balance:.2f}")
            print(f"Transferecia enviada exitosamente a cliente {client.accountHolder} por {amount:.2f}.  \nNuevo saldo actual: {self.balance:.2f}, sobregiro utilizaado: {self.overcharge - (self.overcharge + self.balance):.2f}\n")
            self.history.append(f"Transferencia enviada a cliente {client.accountHolder} por {amount:.2f}")
        else:
            print(f"Cantidad {amount:.2f} supera el monto disponible para transferir. Disponible para retirar: {self.overcharge:.2f}\n")
            self.history.append(f"Operación rechazada por fondos insuficientes.")   
    
    def getOvercharge(self):
        return self.overcharge

    def applyAccountMaintenance(self):
        previousBalance = self.balance
        self.balance -= self.balance * self.maintenance/100
        newBalance = self.balance
        self.history.append(f"Comisión aplicada del {self.maintenance}%, debitando {previousBalance - newBalance:.2f} de la cuenta del cliente.")
        print(f"Aplicada comisión del {self.maintenance:.2f}% por manteniminto de la cuenta, nuevo saldo actual de cliente {self.accountHolder} : {self.balance:.2f}\n")

    def showAvailableOverchage(self):
        if self.balance > 0:
            print(f"Sobregiro de cliente {self.accountHolder} es de {self.overcharge:.2f}\n")
        else:
            print(f"Sobregiro de cliente {self.accountHolder} es de {self.overcharge + self.balance:.2f}\n")

class SavingsAccount(BankAccount):
    def __init__(self, accountHolder, balance, interests=1):
        super().__init__(accountHolder, balance)
        self.interests = interests

    def withdraw(self, amount):
        super().withdraw(amount)
        self.comissions += amount * 2/100
        print(f"Se ha generado comisión por retiro de dinero por 2% del total retirado: {amount * 2/100:.2f}. \n")
    
    def applyInterests(self):
        print(f"Se han abonado {self.balance * self.interests / 100:.2f} a cuenta de cliente {self.accountHolder} por concepto de intereses.\n")
        self.history.append(f"Abonados {self.balance * self.interests / 100:.2f} por concepto de intereses.")
        self.balance += self.balance * self.interests / 100

    def transfer(self, amount, client):
        super().transfer(amount, client)
        self.comissions += amount * 2 / 100

    def applyAccountMaintenance(self):
        self.history.append("Transacción inválida.")
        return print(f"Cuenta de cliente {self.accountHolder} no genera comisiones por mantenimiento.\n")
    
    def showAvailableOverchage(self):
        return print(f"Las cuentas Ahorro no disponen de sobregiro.\n")



client1 = CurrentAccount("Ana Lopez", 50, 50, 0.3) 
client2 = CurrentAccount("Luis Parra", 70, 50, 0.4)
client3 = SavingsAccount("Jesus Farias", 100, 2)
client4 = SavingsAccount("Gonzalo Peña", 100, 1)

clients = [client1, client2, client3, client4]

for client in clients:
    for _ in range (10):
        operation = random.randint(1,4)
        amount = random.randint(0, 100) + random.randint(0, 999) /100
        if operation == 1:
            client.withdraw(amount)
        elif operation == 2:
            client.deposit(amount)
        elif operation == 3:
            client.applyInterests()
        elif operation == 4:
            client.applyAccountMaintenance()

for client in clients:
    for _ in range(10):
        account = random.randint(0, 3)
        amount = random.randint(15,50)
        transferTo = clients[account]
        client.transfer(amount, transferTo)
    client.showClientHistory()

for client in clients:
    client.showBalance()
    client.showAvailableOverchage()
    client.showComissions()
    client.applyInterests()
    client.applyAccountMaintenance()

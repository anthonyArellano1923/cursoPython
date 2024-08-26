'''
	1.	Crea una clase llamada CuentaBancaria que represente una cuenta bancaria.
	2.	Atributos de la clase:
	•	titular: El nombre del titular de la cuenta.
	•	saldo: El saldo actual de la cuenta bancaria (inicializado en 0).
	•	historial_transacciones: Una lista que almacena el historial de transacciones realizadas (depósitos y retiros).
	3.	Métodos de la clase:
	•	depositar(cantidad): Recibe una cantidad y la añade al saldo de la cuenta. También registra la transacción en el historial.
	•	retirar(cantidad): Recibe una cantidad y la resta del saldo de la cuenta, si hay suficiente saldo. Si no hay suficiente saldo, muestra un mensaje indicando que la operación no es posible. También registra la transacción en el historial si es exitosa.
	•	mostrar_saldo(): Muestra el saldo actual de la cuenta.
	•	mostrar_informacion(): Muestra el nombre del titular y el saldo actual.
	•	mostrar_historial(): Muestra el historial completo de transacciones.
	•	aplicar_interes(tasa): Aplica una tasa de interés al saldo actual de la cuenta y actualiza el saldo.
	4.	Prueba tu clase:
	•	Crea una instancia de CuentaBancaria para un titular llamado “Ana López”.
	•	Realiza una serie de depósitos, retiros, y aplica interés, mostrando el historial después de cada operación.
'''
import os
import random
os.system("clear")

class BankAccount:
    def __init__(self, accountHolder, maintenance=0.5, balance=0, interests=1):
        self.accountHolder = accountHolder
        self.balance = balance
        self.interests = interests
        self.maintenance = maintenance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("La cantidad a girar debe ser un número positivo o mayor a cero.")
            return 
        self.balance += amount
        self.history.append(f"Depósito recibido por {amount:.2f}")
        print(f"Depósito recibido en cuenta de cliente {self.accountHolder} por {amount}. \nNuevo saldo actual: {self.balance:.2f}") 

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
        print(f"Transferecia enviada exitosamente a cliente {client.accountHolder} por {amount:.2f}.  \nNuevo saldo actual: {self.balance:.2f}")


    def showBalance(self):
        return print(f"Saldo actual de cliente {self.accountHolder} {self.balance:.2f}")
    
    def showClientInfo(self):
        return print(f"Titular: {self.accountHolder} \nSaldo actual: {self.balance:.2f} \nIntereses apicados de {self.interests:.2f}% \n")

    def showClientHistory(self):
        if len(self.history) > 0:
            print(f"Mostrando historial de cliente {self.accountHolder}:")
            for movement in self.history:
                print(f"  -{movement}")
            print()
        else:
            print(f"No hay movimientos en la cuenta de cliente {self.accountHolder} \n")

    def applyAccountMaintenance(self):
        previousBalance = self.balance
        self.balance -= self.balance * self.interests/100
        newBalance = self.balance
        self.history.append(f"Comisión aplicada del {self.maintenance}%, debitando {previousBalance - newBalance:.2f} de la cuenta del cliente.")
        print(f"Aplicada comisión del {self.maintenance:.2f}% por manteniminto de la cuenta, nuevo saldo actual de cliente {self.accountHolder} : {self.balance:.2f}")
    
    def applyInterests(self):
        previousBalance = self.balance
        self.balance += self.balance * self.interests/100
        newBalance = self.balance
        self.history.append(f"Intereses aplicados del {self.interests:.2f}%, abonando {- previousBalance + newBalance:.2f} a la cuenta del cliente.")
        print(f"Aplicado intereses del {self.interests}%, nuevo saldo actual de cliente {self.accountHolder} : {self.balance:.2f}")

client1 = BankAccount("Ana López")
client2 = BankAccount("María Pérez", 10000, 10)
client3 = BankAccount(interests=12, accountHolder="Jhon Martinez", balance=1000)
clients = [client1, client2, client3]

for client in clients:
    client.showClientInfo()
    client.showClientHistory()

for client in clients:
    client.withdraw(10000)
    client.showClientHistory()

for client in clients:
    client.deposit(15000)
    client.showClientHistory()

for _ in range(30):
    operation = random.randint(1, 4)
    amount = random.randint(100, 50000) + random.randint(1, 999)/100
    if operation == 1:
        client1.deposit(amount)
    elif operation == 3:
        client1.applyAccountMaintenance()
    elif operation == 4:
        client1.applyInterests()
    else:
        client1.withdraw(amount)
    
    print()

client1.showBalance()

client1.transfer(10000, client2)
client1.showClientHistory()
client2.showClientHistory()
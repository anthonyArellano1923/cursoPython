#Creación de clases y métodos de clases.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi, my name is {self.name} and i'm {self.age} years old.")

person1 = Person('Maria', 30)
person2 = Person('Jose', 27)
person3 = Person('Fiona', 43)

person1.greet()
person2.greet()
person3.greet()

#Clase BankAccount

class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
        self.isActive = True
    
    def deposit(self, amount):
        if self.isActive == True:
            self.balance += amount
            print(f"Se han depositado {amount} a la cuenta de {self.accountHolder}. Saldo actual: {self.balance}.")
        else:
            print(f"La cuenta de {self.accountHolder} está inactiva, no se pueden hacer depósitos.")
    
    def withdraw(self, amount): 
        if self.isActive == True and amount < self.balance:
            self.balance -= amount
            print(f"Se han retirado {amount} de la cuenta de {self.accountHolder}. Saldo actual: {self.balance}.")
        elif self.isActive == True and amount > self.balance:
            print(f"Cantidad que desea retirar ({amount}) excede el saldo actual: {self.balance}")
        else:
            print(f"La cuenta de {self.accountHolder} está inactiva, no se pueden hacer retiros.")
    
    def deactivateAccount(self):
        if self.isActive == True:
            self.isActive == False
            print(f"Cuenta de {self.accountHolder} ha sido desactivada exitosamente.")
        else:
            print(f"Cuenta de {self.accountHolder} ya está inactiva.")
    
    def activateAccount(self):
        if self.isActive == False:
            self.isActive == True
            print(f"Cuenta de {self.accountHolder} ha sido activada exitosamente.")
        else:
            print(f"Cuenta de {self.accountHolder} ya está activa.")
    
    def showBalance(self):
        print(f"Saldo actual: {self.balance}")

account1 = BankAccount('Anita López', 2365)
account2 = BankAccount('Frank Suaez', 450)
account3 = BankAccount('Gabriela Sarmiento', 2365)

account1.activateAccount()
account1.deposit(1500)
account2.withdraw(500)
account2.deposit(1000)
account3.deactivateAccount()
account2.withdraw(1440)
account3.deactivateAccount()
account1.showBalance()
account3.withdraw(2365)

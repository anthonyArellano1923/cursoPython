#Gestión de biblioteca con POO

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availible = True
    
    def borrowBook(self, user):
        if self.availible: 
            self.availible = False
            print(f"El libro {self.title} ha sido prestado a {user}.")
        else:
            print(f"Libro {self.title} no disponible para préstamo.")
    
    def recieveBook(self, user):
        if self.availible == False:
            self.availible = True
            print(f"{user} ha devuelto {self.title} a la biblioteca y está de nuevo disponible para su préstamo.")
        else:
            print(f"{self.title} se encuentra en la biblioteca.")

class User:
    def __init__(self, name, iD):
        self.name = name
        self.iD = iD
        self.booksBorrowed = []
    
    def getBook(self, book):
        if book.availible:
            book.borrowBook(self.name)
            self.booksBorrowed.append(book)
        else:
            if book not in self.booksBorrowed:
                print(f"Libro {book.title} no está disponible.")
            else:
                print(f"Ya tienes {book.title} en tu poder.")
    
    def returnBook(self, book):
        if book in self.booksBorrowed:
            book.recieveBook(self.name)
            self.booksBorrowed.remove(book)
        else:
            print(f"Libro {book.title} no está en tu poder.")
    
    def showUserBooks(self):
        print()
        if len(self.booksBorrowed) > 0:
            print(f"Libros prestados a usuario {self.name}:")
            for book in self.booksBorrowed:
                 print(f"    - {book.title}")
        else:
            print(f"El usuario {self.name} no tiene libros prestados.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def registerUser(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"Usuario {user.name} añadido con éxito a base de datos.")
        else:
            print(f"Usuario {user.name} ya está registrado.")
    
    def registerBook(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Libro {book.title} añadido con éxito a base de datos.")
        else:
            print(f"Libro {book.title} ya está registrado.")
    
    def showUsers(self):
        print()
        if len(self.users) > 0:
            for user in self.users:
                print(f"Usuario: {user.name}")
        else:
            print("No hay usuarios registrados en la bibloteca")

    def showAvailibleBooks(self):
        print()
        booksAvailible = 0
        for book in self.books:
            if book.availible == True:
                booksAvailible +=1
        if booksAvailible > 0:
            print('Libros disponibles:')
            for book in self.books:
                if book.availible:
                    print(f"   -{book.title}. Por: {book.author}")
        else:
            print("No hay libres disponibles para préstamo")
    
    def showBorrowedBooks(self):
        print()
        booksAvailible = 0
        for book in self.books:
            if book.availible == True:
                booksAvailible +=1
        if booksAvailible == len(self.books):
            print("Todos los libros están disponibles.")
        else:
            for user in self.users:
                if len(user.booksBorrowed) > 0 :
                    user.showUserBooks()                  
            
book1 = Book("Cien años de soledad","Gabriel García Márquez")
book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
book3 = Book("1984", "George Orwell")
book4 = Book("Matar a un ruiseñor", "Harper Lee")
book5 = Book("El gran Gatsby", "F. Scott Fitzgerald")

user1 = User("Ana Pérez", "001")
user2 = User("Luis García", "002")
user3 = User("Marta Fernández", "003")
user4 = User("Javier Gómez", "004")
user5 = User("Claudia Rodríguez", "005")

library = Library()

users = [user1, user2, user3, user4, user5]
books = [book1, book2, book3, book4, book5]

for element in users:
    library.registerUser(element)

for element in books:
    library.registerBook(element)

library.showUsers()
print()
library.showAvailibleBooks()
print()
user2.returnBook(book1)
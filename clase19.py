#Subclases de Exception
def conjuntoVacio89(): #Probando que pass hace que esto no exista
    pass 


def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)
    

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
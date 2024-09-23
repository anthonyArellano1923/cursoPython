#Batalla naval!
import os, random, copy
os.system('clear')
board = [['*' for x in range(10)] for y in range(10)]

#Imprimiendo tablero###################
def printBoard(board):
    for row in board:
        print(' '.join(map(str, row)))
#######################################


class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
        
    def place_ship(self, start_row, start_column, direction, board):
        if direction == 'h': #Verifcicando si barco cabe en el mapa
            if start_column + self.size > 10:
                return False
        else:
            if start_row + self.size > 10:
                return False
        
        if direction == 'h': #Verificando si el espacio está ocupado
            for column in range(start_column, start_column + self.size):
                if board[start_row][column] != '*':
                    return False
        else:
            for row in range(start_row, start_row + self.size):
                if board[row][start_column] != '*':
                    return False
        
        if direction == 'h': #Dibujando mapa y guardando sus posiciones.
            for column in range(start_column, start_column + self.size):
                self.positions.append([start_row, column])
                board[start_row][column] = self.name[0]
        else:
            for row in range(start_row, start_row + self.size):
                self.positions.append([row, start_column])
                board[row][start_column] = self.name[0] 
        return True  
        
    def hit(self):#Incrementa contador de hits del barco, envía mensaje si es destruido.
        self.hits += 1
        if self.hits == self.size:
            print(f"El barco {self.name} ha sido destruido.")
            return True
        return False

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:

    def __init__(self, name):
        self.name = name
        self.board = copy.deepcopy(board)
        self.ships = []
        self.hits = copy.deepcopy(board)
    
    def place_ship(self):
        ships_to_place = [Destroyer(), Submarine(), Battleship()]

        for ship in ships_to_place:
            while True:
                try:
                    print(f"Iniciando despliegue de {ship.name}, tamaño: {ship.size}")
                    row = int(input('Introduzca fila inicial: '))
                    column =  int(input('Introduzca fila inicial: '))
                    while True:
                        direction = input('Define una orientación [H/V]: ')
                        if direction.lower() != 'h' and direction.lower() != 'v':
                            print('Introduzca una opción válida: H o V:')
                        else:
                            break
                    if ship.place_ship(row, column, direction, self.board):
                        self.ships.append(ship)
                        break
                    else:
                        print(f"No fue posible desplegar en [{row, column}], intente otro sitio.")
                except ValueError:
                    print('Introduzca número válido')
    
    def print_board(self):
        for row in self.hits:
            print(' '.join(row))
    
    def attack(self, player):
        print("Iniciando ataque:")
        while True:
            try:
                row = int(input('Indica la fila: '))
                column = int(input('Indica la columna: '))
                if row <= 10 and row > 0 and column <= 10 and column > 0:
                    print(f"Lanzando bombas en [{row, column}]!!")
                    break
                else:
                    print(f"Los valores de fila ({row}) y columna ({column}) deben ser mayores a 0 y no mayores a 10")
            except ValueError:
                print('Introduzca números válidos.')
        
        if player.board[row][column] != '*':
            player.board[row][column] = 'X'
            self.hits[row][column] = 'X'
            shoot = [row,column]
            print('Impacto exitoso!')
            for ship in player.ships:
                if shoot in ship.positions:
                    ship.hit()
                    break #Verificar si este código es correcto para salir del bucle 'for'.
                #queda pendiente verificar si jugador aún tiene barcos y finalizar el juego en cuanto el jugador se quede sin estos. Además, continuar con la lógica de las instruciones del ejercicio. Quedé en el paso 4, último ítem.
        else:
            self.hits[row][column] = '@'
            print('Impacto fallido!')

    
            
 
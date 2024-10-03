#Batalla naval!
import os, random, copy, time, sys
os.system('clear')
board = [['*' for x in range(10)] for y in range(10)]

#Imprimiendo tablero###################
def printBoard(board):
    for row in board:
        print(' '.join(map(str, row)))
#######################################

#Obtener Coordenadas del ataque###############################################################
def getCoordinates():
    while True: #Obtener ataques de jugadores
            try:
                row = int(input('Indica la fila (0-9): '))
                column = int(input('Indica la columna (0-9): '))
                if 0 <= row <= 9 and 0 <= column <= 9:
                    print(f"Lanzando bombas en [{row, column}]!!")
                    return row, column
                else:
                    print(f"Los valores de fila ({row}) y columna ({column}) deben ser mayores a 0 y menores a 10")
            except ValueError:
                print('Introduzca números válidos.')
##############################################################################################


#Tiempo de espera######################
def waitTime():
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.2)
    print()
#######################################

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
        
    def place_ship(self, start_row, start_column, direction, board):
        if direction == 'h': #Verifcicando si barco cabe en el mapa
            if start_column + self.size > 9 + 1:
                return False
        else:
            if start_row + self.size > 9 + 1:
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
    
    def deployment_choice(self):
        while True:
            deployment_choice = input('Ubicación de flota: \n[1] -Manual.\n[2] -Aleatorio.\n')
            if deployment_choice == '1':
                self.p_place_ship()
                break
            elif deployment_choice == '2':
                self.r_place_ship()
                break
            else:
                pass

    def p_place_ship(self):
        ships_to_place = [Destroyer(), Submarine(), Battleship()]
        print('Inicializando.')
        '''waitTime()'''
        print(f"{self.name} creado. Creando ejército.")
        '''waitTime()'''
        for ship in ships_to_place:
            while True:
                try:
                    print(f"Iniciando despliegue de {ship.name}, tamaño: {ship.size}")
                    row = int(input('Introduzca fila inicial: '))
                    column =  int(input('Introduzca columna inicial: '))
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
        print('Flota desplegada con éxito. Mostrando Distribución:')
        printBoard(self.board)
        input('Presione enter para continuar.')

    def r_place_ship(self):
        ships_to_place = [Destroyer(), Submarine(), Battleship()]
        directions = ['h', 'v']
        print('Inicializando.')
        waitTime()
        if self.name == 'PC':
            print(f"PC habilitado para luchar. Creando ejército.")
        else:
            print(f"{self.name} creado. Creando ejército.")
        waitTime()
        for ship in ships_to_place:
            while True:
                row, column, direction = random.randint(0,9), random.randint(0,9), random.choice(directions)
                if ship.place_ship(row, column, direction, self.board):
                    self.ships.append(ship)
                    print(f"{ship.name} de {self.name} desplegado en [{row, column}]")
                    waitTime()
                    break
        print(f'Flota de {self.name} desplegada con exito!')
        printBoard(self.board)

    def print_board(self):
        for row in self.hits:
            print(' '.join(row))
       
    def attack(self, player):
        os.system('clear')
        print(f"{self.name} atacando a {player.name}")
        if self.name != 'PC':
            printBoard(self.hits)

        if self.name == 'PC':
            row, column = random.randint(0,9), random.randint(0,9)
        else:
            row, column = getCoordinates()
        
        if player.board[row][column] != '*' and self.hits[row][column] not in  ['X', '@']: #Evaluar el lugar de impacto.
            player.board[row][column] = 'X'
            self.hits[row][column] = 'X'
            shoot = [row,column]
            print('Impacto exitoso!')
            print(f"Ataque realizado en [{row},{column}]")
            for ship in player.ships:
                if shoot in ship.positions:
                    if ship.hit():
                        for s in player.ships:
                            if s.name == ship.name:
                                player.ships.remove(s)
                    break
        elif player.board[row][column] != '*' and self.hits[row][column] in ['@', 'X']:
            print(f"Ya has atacado en [{row}.{column}], pierdes tu turno!")
        else:
            self.hits[row][column] = '@'
            print('Impacto fallido!')
            print(f"Ataque realizado en [{row},{column}]")

        printBoard(self.hits)
        input('Presiona ENTER para continuar')
        return 
                    
    def all_ships_sunk(self):
        if len(self.ships) <= 0: #Verificar si jugador no tiene barcos.
            print(f"Todos los barcos de {self.name} han sido hundidos.")
            return True
        else:
            return False

    def getName(self):
        return self.name

class BattleshipGame:
    def __init__(self):
        self.player1 = Player('Player 1')
        self.player2 = ''


    def play(self):
        print('Bienvendio a esta batalla naval!')
        '''waitTime()
        waitTime()'''
        self.player2 = self.pick_2nd_player()
        print('Iniciando batalla!')
        self.player1.deployment_choice()
        if self.player2.getName() == 'Player 2':
            self.player2.deployment_choice()
        else:
            self.player2.r_place_ship()
        while True:
            self.player1.attack(self.player2)
            if self.player2.all_ships_sunk():
                break
            self.player2.attack(self.player1)
            if self.player1.all_ships_sunk():
                break
   
    def pick_2nd_player(self):
        choice = ''
        while choice.lower() != 'pc' and choice.lower() != '2':
            choice = input('Elije al segundo jugador:\n-[1] PC.\n-[2] 2do jugador.\n ')
            if choice != '1' and choice != '2':
                print("Elije una opción válida, [1] PC o [2] 2do jugador: ")
            else:
                break
        if choice == '2':
            return Player('Player 2')
        else:
            return Player('PC')

            
        

            


        

game = BattleshipGame()
game.play()     

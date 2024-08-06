#piedra, papel tijera
import os
import random

p1 = 0
pc = 0

def clear_console():
    # Clear console for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear console for Unix (Linux/Mac)
    else:
        _ = os.system('clear')


def random_play():
    play = random.randint(0,2)
    return play


def player_play():
    player = input('Tu jugada -> [0] Piedra, [1] Papel, [2] Tijera: ')
    if player == '0' or player == '1' or player == '2':
        clear_console()
        return int(player)
    else:
        print('Introduzca una opción válida.')
        return player_play()
    

def match(p1_play, pc_play, p1, pc):
    print(f"Jugador: {plays[p1_play]} \nPC: {plays[pc_play]}")
    if p1_play == 0 and pc_play == 2 or p1_play == 1 and pc_play == 0 or p1_play == 2 and pc_play == 1:
        print("El jugador gana el enfrentamiento!")
        p1 += 1
    elif p1_play == pc_play:
        print("Empate.")
    else:
        print('La PC gana el enfrentamiento.')
        pc += 1
    return p1, pc

clear_console()

plays = ['Piedra', 'Papel', 'Tijera']

print('Bienvenido a este minijuego de piedra, papel y tijeras.')
print('Gana el mejor de 3.')
print()

while p1 < 2 and pc < 2:
    p1_play = player_play()
    pc_play = random_play()
    p1, pc = match(p1_play, pc_play, p1, pc)
    print(f"Victorias: Jugador({p1}) PC({pc})")
    print()

if p1 == 2:
    print('El jugador gana la partida!')
else:
    print('La PC ha ganado la partida.')
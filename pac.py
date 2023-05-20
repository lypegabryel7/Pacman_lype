import time
import random
import os

num_row = 13
num_column = 15

pacman_pos = [random.randint(0, num_row), random.randint(0, num_column)]
comida_pos = [random.randint(0, num_row), random.randint(0, num_column)]

matriz = [['.'for column in range(num_column)] for row in range(num_row)]
matriz[pacman_pos[0]][pacman_pos[1]] = 'o'
matriz[comida_pos[0]][comida_pos[1]] = 'X'

def show_matriz():
    for linha in matriz:
        print(' '.join(linha))
    print()

def mover_pac():
    if pacman_pos[0] < comida_pos[0]:
        pacman_pos[0] += 1
    elif pacman_pos[0] > comida_pos[0]:
        pacman_pos[0] -= 1
    elif pacman_pos[1] < comida_pos[1]:
        pacman_pos[1] += 1
    elif pacman_pos[1] > comida_pos[1]:
        pacman_pos[1] -= 1
def remove_o(): 
    if matriz[pacman_pos[0]][pacman_pos[1]-1] == 'o': matriz[pacman_pos[0]][pacman_pos[1]-1] = '.'
    elif matriz[pacman_pos[0]-1][pacman_pos[1]-1] == 'o': matriz[pacman_pos[0]-1][pacman_pos[1]-1] = '.'
    elif matriz[pacman_pos[0]-1][pacman_pos[1]] == 'o': matriz[pacman_pos[0]-1][pacman_pos[1]] = '.'
    elif matriz[pacman_pos[0]+1][pacman_pos[1]] == 'o': matriz[pacman_pos[0]+1][pacman_pos[1]] = '.'
    elif matriz[pacman_pos[0]+1][pacman_pos[+1]] == 'o': matriz[pacman_pos[0]+1][pacman_pos[+1]] = '.'
    elif matriz[pacman_pos[0]][pacman_pos[1]+1] == 'o': matriz[pacman_pos[0]][pacman_pos[1]+1] = '.' 

while pacman_pos != comida_pos:
    
    mover_pac()
    
    pacman_pos[0] = max(0, min(pacman_pos[0], num_column+1)) 
    pacman_pos[1] = max(0, min(pacman_pos[1], num_row+1)) 
    matriz[pacman_pos[0]][pacman_pos[1]] = 'O' if pacman_pos == 'o' else 'o'
    
    remove_o()

       
    show_matriz()
    time.sleep(0.5)
    os.system('cls')
print('sim')
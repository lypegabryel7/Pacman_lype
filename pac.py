import time
import random
import os
import keyboard

num_row = 15
num_column = 17



matriz = [['.'for column in range(num_column)] for row in range(num_row)]
pacman_pos = [random.randint(0, num_column), random.randint(0, num_row)]
comida_pos = [random.randint(0, num_column), random.randint(0, num_row)]
matriz[pacman_pos[0]][pacman_pos[1]] = 'o'
matriz[comida_pos[0]][comida_pos[1]] = 'X'
score = 0
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

while keyboard.is_pressed('Esc') == False:
    
    mover_pac()
     
    matriz[pacman_pos[0]][pacman_pos[1]] = 'O' if pacman_pos == 'o' else 'o'
    
    remove_o()
    show_matriz()
    time.sleep(0.25)
    os.system('cls')
    if pacman_pos == comida_pos: comida_pos = [random.randint(0, num_column-2), random.randint(0, num_row-2)]
    matriz[comida_pos[0]][comida_pos[1]] = 'X'
    if pacman_pos == comida_pos: score += 1
print(f'Parabéns! Sua pontuação foi: {score}')
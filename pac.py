import time
import random

num_row = 15
num_column = 10

pacman_pos = [random.randint(0, num_column - 1), random.randint(0, num_row-1)]
comida_pos = [random.randint(0, num_column - 1), random.randint(0, num_row-1)]

matriz = [['.'for row in range(num_row)] for column in range(num_column)]
matriz[pacman_pos[0]][pacman_pos[1]] = 'o'
matriz[comida_pos[0]][comida_pos[1]] = 'X'

def show_matriz():
    for linha in matriz:
        print(' '.join(linha))
    print()

show_matriz()
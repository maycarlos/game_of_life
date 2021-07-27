#!/usr/bin/python

import sys
import os
import cursor
import numpy as np
from time import sleep
from colorama import init, Fore

init(autoreset=True)

ALIVE = 1
DEAD = 0
COLUMNS, LINES  = os.get_terminal_size(0)

def dead_state(width: int, height: int) -> np.ndarray:

    return np.zeros((width, height), dtype=np.int0)

def random_state(width: int, height: int) -> np.ndarray:

    state = dead_state(width, height)

    with np.nditer(state, op_flags=['readwrite']) as it:
        for i in it:
            if np.random.random() <= 0.35:
                i[...] = ALIVE
            else:
                i[...] = DEAD

    return state

def cell_status(coords: tuple, board_state: np.ndarray) -> DEAD | ALIVE:
    # Estava a complicar demasiado o problema, no exemplo está muito mais simples

    height = board_state.shape[1]
    width = board_state.shape[0]
    x = coords[0]
    y = coords[1]
    neightbors_alive = 0

    for i in range((x-1), (x+1)+1):
        if i < 0 or i >= width: continue

        for j in range((y-1), (y+1)+1):
            if j < 0 or j >= height: continue
            if i == x and j == y: continue

            if board_state[i,j] == ALIVE:
                neightbors_alive += 1

    if board_state[x,y] == ALIVE:
        if neightbors_alive <= 1:
            return DEAD
        elif neightbors_alive <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if neightbors_alive == 3:
            return ALIVE
        else:
            return DEAD

def next_board_state(board_state: np.ndarray) -> np.ndarray:
    """
    Regras:
        1- Uma célula viva com 0 ou 1 vizinho morre.
        2- Uma célula viva com 2 ou 3 vizinhos continua viva.
        3- Uma célula viva com mais do que 3 vizinhos morre.
        4- Uma célula morta com 3 vizinhos vivos torna-se viva.
    """

    next_state = dead_state(*board_state.shape)

    for x in range(board_state.shape[0]):
        for y in range(board_state.shape[1]):
            next_state[x,y] = cell_status((x,y), board_state)
    return next_state

def render(board_state) -> None:

    # Tive que mudar para uma lista porque não sabia trabalhar muito bem com chararray do numpy
    render_state = board_state.tolist()

    dead_or_alive = {
        DEAD: ' ',
        ALIVE: u"\u2588"
    }

    renderized = [''.join([dead_or_alive[render_state[x][y]] * 2 for x in range(len(render_state))]) for y in range(len(render_state[0]))]

    print(Fore.YELLOW + "\n".join(renderized))

def main() -> None:
    # Tive que dividir o numero de colunas por dois porque está a dar um espaço a mais a pixels adjecentes
    clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    cursor.hide()
    game = random_state(COLUMNS//2, LINES)
    render(game)
    while True:
        try:
            render(game := next_board_state(game))

            sleep(1/75)
            clear()
        except KeyboardInterrupt as e:
            cursor.show()
            clear()
            sys.exit(e)

if __name__ == "__main__":
    main()
#!/usr/bin/python

import numpy as np
ALIVE = 1
DEAD = 0

def dead_state(width, height) -> np.ndarray:

    return np.zeros((width, height), dtype=np.int0)

def random_state(width, height) -> np.ndarray:

    state = dead_state(width, height)

    with np.nditer(state, op_flags=['readwrite']) as it:
        for i in it:
            if np.random.random() >= 0.5:
                i[...] = ALIVE
            else:
                i[...] = DEAD

    return state

def next_board_state(board_state) -> np.ndarray:
    """
    Regras:
        1- Uma célula viva com 0 ou 1 vizinho morre.  
        2- Uma célula viva com 2 ou 3 vizinhos continua viva.  
        3- Uma célula viva com mais do que 3 vizinhos morre.  
        4- Uma célula morta com 3 vizinhos vivos torna-se viva.  
    """
    # TODO fazer a soma dos valores do vizinhos e alterar o estado da celula consoante o resultado
    # se for -∞, 1]  celula = DEAD
    # se for  [2, 3] pass
    # se for  ]3, +∞ celula = dead
    # se o celulad DEAD e com soma = 3 celula = ALIVE

    next_state = dead_state(*board_state.shape)

    for x in range(len(board_state)):
        for y in range(len(board_state[0])):

            if y == 0:
                if x == 0:
                    status = np.sum([board_state[x,y+1],board_state[x+1,y],board_state[x+1,y+1]])

                elif x == board_state.shape[0]-1:
                    status = np.sum([board_state[x-1,y],board_state[x,y+1],board_state[x-1,y+1]])

                else:
                    status = np.sum([board_state[x-1,y],board_state[x+1,y],board_state[x-1,y+1],board_state[x,y+1]], board_state[x+1,y+1])

            elif y == board_state.shape[1]-1:
                if x == 0:
                    status = np.sum([board_state[x,y-1],board_state[x+1,y],board_state[x+1,y-1]])

                elif x == board_state.shape[0]:
                    status = np.sum([board_state[x-1,y],board_state[x-1,y-1],board_state[x,y-1]])

                else:
                    status = np.sum([board_state[x-1,y],board_state[x+1,y],board_state[x-1,y-1],board_state[x,y-1]], board_state[x+1,y-1])
            else:
                status = np.sum([board_state[x-1,y-1],board_state[x,y-1],board_state[x+1,y-1],
                    board_state[x-1, y],board_state[x+1,y],
                    board_state[x-1,y+1],board_state[x,y+1],board_state[x+1,y+1]])

            if board_state[x,y] == ALIVE and status <= 1:
                next_state[x,y] = DEAD #UNDER_POP

            elif board_state[x,y] == ALIVE and 2 <= status <= 3:
                pass

            elif board_state[x,y] == ALIVE and status > 3:
                next_state[x,y] = DEAD #OVER_POP

            elif board_state[x,y] == DEAD and status == 3:
                next_state[x,y] = ALIVE

    return next_state

def render(board_state) -> None:

    render_state = board_state.tolist()

    dead_or_alive = {
        DEAD: ' ',
        ALIVE: u"\u2588"
    }

    renderized = [''.join([dead_or_alive[render_state[x][y]] * 2 for x in range(len(render_state))]) for y in range(len(render_state[0]))]

    print("\n".join(renderized))

def main():
    coisa = random_state(3,3)

    render(coisa)
    print("\n")
    render(next_board_state(coisa))

if __name__ == "__main__":
    main()

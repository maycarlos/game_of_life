#!/usr/bin/python

import numpy as np
ALIVE = 1.0
DEAD = 0.0

def dead_state(width, height):

    return np.zeros((width, height))

def random_state(width, height):

    state = dead_state(width, height)

    with np.nditer(state, op_flags=['readwrite']) as it:
        for i in it:
            if np.random.random() >= 0.5:
                i[...] = ALIVE
            else:
                i[...] = DEAD

    return state

def render(board_state):

    render_state = board_state.tolist()

    dead_or_alive = {
        DEAD: ' ',
        ALIVE: u"\u2588"
    }

    renderized = [''.join([dead_or_alive[render_state[x][y]] * 2 for x in range(len(render_state))]) for y in range(len(render_state[0]))]

    print("\n".join(renderized))

def main():

    render(random_state(5,5))
    print("\n")
    render(random_state(10,10))
    print("\n")
    render(random_state(20,20))

if __name__ == "__main__":
    main()

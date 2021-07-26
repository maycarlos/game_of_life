#!/usr/bin/python

import numpy as np

ALIVE = 1
DEAD = 0

def dead_state(width, height):
    return np.zeros((width, height))

def random_state(width, height):
    state = dead_state(width, height)

    for i in range(len(state[:,0])):
        for j in range(len(state[0,:])):
            if np.random.random() >= 0.5:
                state[i,j] = ALIVE
            else:
                state[i,j] = DEAD

    return state


def main():
    print(random_state(5,5))

if __name__ == "__main__":
    main()

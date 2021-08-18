#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        p1, p2 = line.strip().split(' ')

        if p1 == 'paper' and p2 == 'rock':
            print('Player 1 wins')

        elif p1 == 'rock' and p2 == 'paper':
            print('Player 2 wins')

        elif p1 == 'rock' and p2 == 'scissors':
            print('Player 1 wins')

        elif p1 == 'paper' and p2 == 'scissors':
            print('Player 2 wins')

        elif p1 == 'scissors' and p2 == 'paper':
            print('Player 1 wins')

        elif p1 == 'scissors' and p2 == 'rock':
            print('Player 2 wins')

        else:
            print('Draw')

if __name__ == '__main__':
    main()

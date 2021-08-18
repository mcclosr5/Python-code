#!/usr/bin/env python3

import sys

def arithmetic(a, b, c=3, d=4):
    return a + b + c + d

def main():

    print(arithmetic(1, 2, 4, 5))
    print(arithmetic(3, 4, 5))
    print(arithmetic(3, 4, d=3))
    print(arithmetic(b=5, a=4, d=2, c=1 ))
if __name__ == '__main__':
    main()

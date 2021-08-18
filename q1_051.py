#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    ls = list(s)
    i = 1
    while i < len(ls):
        ls[i - 1], ls[i] = ls[i], ls[i - 1]
        i += 2
    print(''.join(ls)

if __name__ == '__main__':
    main()

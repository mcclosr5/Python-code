#!/usr/bin/env python3

import sys


def main():
    s = sys.argv[1]
    n = int(sys.argv[2])
    i = len(s) - 1
    while n > 0:
        s = s[1:] + s[0]
        n = n - 1
    print(s)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys
def main():
    a = []
    for line in sys.stdin:
        line = line.strip().split()
        for word in line:
            for c in word[:]:
                if c not in a:
                    a.append(c)
        if len(a) == 2 or len(a) < 2:
            print(0)
        elif len(a) > 2:
            print(len(a) - 2)
        a = []

if __name__ == '__main__':
    main()

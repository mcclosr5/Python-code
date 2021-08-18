#!/usr/bin/env python3

import sys

def main():
    a = []
    for line in sys.stdin:
        line = line.strip()
        a.append(int(line))
    time = a[1] - a[0]
    print(time)

if __name__ == '__main__':
    main()

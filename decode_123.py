#!/usr/bin/env python

import sys

def main():
    vowels = 'aeiou'
    for line in sys.stdin:
        a = line.strip()
        a = a.split(maxsplit=0)
        b = []
        for word in line:
            for c in word:
                b.append(c)
        i = 0
        while i < len(b):
            if b[i] in vowels:
                b.pop(i + 1)
                b.pop(i + 1)
            i += 1
        b = ''.join(b)
        b = b.strip('\n')
        print(b)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def vow(s):
    return [c for c in s if c in vowels]

def main():
    for line in sys.stdin:
        r = line.strip().lower()
        if vow(r) == vowels:
            print(line.strip())

if __name__ == '__main__':
    main()

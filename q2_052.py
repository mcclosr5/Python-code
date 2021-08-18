#!/usr/bin/env python3

import sys

evil = ['e', 'v', 'i', 'l']

def evils(s):
    return [c for c in s if c in evil]

def main():
    for line in sys.stdin:
        low = line.strip().lower()
        if evils(low) == evil:
            print(line.strip())

if __name__ == '__main__':
    main()

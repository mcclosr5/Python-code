#!/usr/bin/env python3

import sys

def camel(s):
    i = 0
    while i < len(s):
        i = 0
        while i < len(s):
            s[i] = s[i][:: - 1]
            s[i] = s[i].capitalize()
            s[i] = s[i][:: - 1]
            i += 1
    return s

def main():
    for line in sys.stdin.readlines():
        line = line.strip().split()
    print(" ".join(camel(line)))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys
def evil(s):
    return [c for c in s if c in 'evil'] == list('evil')
def main():
    word_list = [line.strip() for line in sys.stdin]
    evil_list = [w for w in word_list if evil(w.lower())]
    print(evil_list)
    for w in evil_list:
        print(w)

if __name__ == '__main__':
    main()

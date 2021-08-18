#!/usr/bin/env python3

import sys

def camel(s):
   i = 0
   while i < len(s):
      words = s[i]
      s[i] = words.capitalize()
      i += 1
   return s
def main():
    for s in sys.stdin.readlines():
        s = s.strip()
        s = s.split()
        print(" ".join(camel(s)))

if __name__ == '__main__':
    main()

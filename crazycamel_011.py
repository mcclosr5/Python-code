#!/usr/bin/env python3

import sys

def caps(words):
   i = 0
   while i < len(words):
      i = 0
      while i < len(words):
         words[i] = words[i][:: - 1]
         words[i] = words[i].capitalize()
         words[i] = words[i][:: - 1]
         i += 1
   return words

def main():
   for line in sys.stdin.readlines():
      line = line.strip()
      line = line.split()
      print(" ".join(caps(line)))

if __name__ == '__main__':
    main()

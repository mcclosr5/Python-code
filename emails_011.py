#!/usr/bin/env python3

import sys

def name(s):
   nums = "0123456789"
   tokens = s.split("@")
   [first, last] = tokens[0].strip(nums).split(".")
   name = first.capitalize() + " " + last.capitalize()
   return name

def main():
   for line in sys.stdin:
      line = line.strip()
      print(name(line))

if __name__ == '__main__':
    main()

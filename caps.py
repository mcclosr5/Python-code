#!/usr/bin/env python3

import sys

def capitals(s):
   c1 = s[0].capitalize()
   c2 = s[-1].capitalize()
   return c1 + s[1:len(s) - 1] + c2
def main():
   for line in sys.stdin:
      s = line.strip()
      if len(s) >= 2:
         print capitals(s)

if __name__ == '__main__':
	main()

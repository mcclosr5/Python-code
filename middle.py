#!/usr/bin/env python3

import sys

def middle(s):
	m = s[len(s) / 2]
	return m

def main():
   for line in sys.stdin:
      line = line.strip()
      if len(line) % 2 != 0:
         print(middle(line))
      else:
      	print("No middle character!")

if __name__ == '__main__':
	main()

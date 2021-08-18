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
   for line in sys.stdin:
      line = line.strip().split()
   print(" ".join(camel(line)))

if __name__ == '__main__':
	main()

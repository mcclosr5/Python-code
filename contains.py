#!/usr/bin/env python3

import sys

def contains(left, right):
	for c in left:
	   if c in right:
	      right = right.replace(c, '', 1)
	   else:
	      return False
	return True

def main():
	for line in sys.stdin:
		[c, s] = line.strip().lower().split()
	print(contains(c, s))

if __name__ == '__main__':
	main()

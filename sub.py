#!/usr/bin/env python3

import sys


def substring(left, right):
    if left in right:
    	return True
    else:
    	return False

def main():
   for line in sys.stdin:
      [left, right] = line.strip().lower().split()
      print(substring(left, right))

if __name__ == '__main__':
	main()
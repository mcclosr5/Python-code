#!/usr/bin/env python3

import sys

def helper(c):
	if c.isupper():
		return c
	else:
		return "0"
def transform(s):
	return ''.join([helper(c) for c in s])

def main():
	s = sys.stdin.read().split()
	for line in s:
	    uppers = transform(line)
	    uppers = uppers.split('0')
	    print(max(uppers, key=len))

if __name__ == '__main__':
	main()

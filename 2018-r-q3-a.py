#!/usr/bin/env python

import sys
s = sys.stdin.readlines()
d = {
	"hello": True,
	"my": True,
	"name": True,
	"is": True,
	"ruadhan": True,
}
i = 0
b = []
while i < len(s):
   if s[i] in d:
      b.append(s[i])
   i = i + 1
print b

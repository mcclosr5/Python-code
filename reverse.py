#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
i = 0
reverse = []
while i < len(s):
   characters = s[i].rstrip()
   reverse.append(characters)
   i = i + 1
   
j = 0
while j < len(reverse):
   print reverse[len(reverse) - j - 1]
   j = j + 1

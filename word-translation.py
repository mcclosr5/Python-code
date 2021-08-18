#!/usr/bin/env python

d = {}

with open("translation.txt") as fd:
   line = fd.readlines()

i = 0
while i < len(line):
   l = line[i].strip().split()
   d[l[0]] = l[1]
   i = i + 1

import sys
words = sys.stdin.readlines()

j = 0
while j < len(words):
   translate = words[j].strip()
   print d[translate]
   j = j + 1

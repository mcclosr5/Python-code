#!/usr/bin/env python

import sys

s = raw_input()
position = sys.argv[1]
a = []
i = 0

while i < len(s):
   j = i
   word = ''

   while j < len(s) and s[j] != ',':
      word = word + s[j]
      j += 1
   a.append(word)

   i = j + 1

p = 0

while p < len(a):
   if a[p] == position:
      print p
   p += 1

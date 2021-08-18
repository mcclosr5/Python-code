#!/usr/bin/env python

import sys

nos = sys.stdin.readlines()

i = 0
while i < len(nos):
   s = nos[i].strip()

   j = 0
   while j < len(s) and s[j] == "0":
      j = j + 1

   if j < len(s):
      print s[j:]
   else:
      print "0"
   i = i + 1

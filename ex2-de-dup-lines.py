#!/usr/bin/env python

s = raw_input()

a = []

i = 0
while s != "end":
   while i < len(a) and a[i] != s:
      i = i + 1
   if not i < len(a):
      a.append(s)
      print s
   s = raw_input()
   i = 0

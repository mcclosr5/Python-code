#!/usr/bin/env python

a = []
s = raw_input()
while s!= "end":
   n = int(s)
   a.append(n)
   p = len(a) - 1
   while 0 < p and n < a[p-1]:
      a[p] = a[p-1]
      p = p - 1
   a[p] = n
   if 10 < len(a):
      a.pop()
   s = raw_input()
print a
#!/usr/bin/env python

i = 0
a = [4, 5, 14, 12]
j = i + 1
while i < len(a):
   if a[i] > a[j]:
      j = i
   i = i + 1
print a[j]

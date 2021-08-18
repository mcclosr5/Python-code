#!/usr/bin/env python#

a = [1, 3, 2, 19, 100, 12]
i = 0
j = i + 1
while i < len(a):
   if a[i] > a[j]:
      j = i
   i = i + 1
print a[j]

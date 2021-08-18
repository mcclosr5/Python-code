#!/usr/bin/env python

maximum = [4, 9, 12, 3]
i = 0
j = i + 1
while i < len(maximum):
   if maximum[i] > maximum[j]:
      j = i
   i = i + 1
print maximum[j]

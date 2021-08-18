#!/usr/bin/env python

totalpos = 0
totalneg = 0
s = 69
while s != 0:
   s = raw_input()
   s = int(s)
   if s < 0:
      totalneg = totalneg + s
   else:
      totalpos = totalpos + s
print totalneg, totalpos

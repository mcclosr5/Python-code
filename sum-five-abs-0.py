#!/usr/bin/env python

total = 0

s = 69
while s != 0:
   s = raw_input()
   s = int(s)
   if s < 0:
      s = (s * -1)
      total = total + s
   else:
      total = total + s
print total

#!/usr/bin/env python

import sys
def reverse(a):
   i = 0
   while i < len(a):
      j = len(a) - 1
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
      i = i + 1
a = sys.argv
print " ".join(a)

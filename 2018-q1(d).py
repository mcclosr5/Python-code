#!/usr/bin/env python

import sys
a = sys. stdin.readlines()
t = 0

i = 0
while i < len(a):
   t = t + int(a[i])
   i = i + 1

v = t / len(a)

i = 0
while i < len(a):
   if a[i] < v:
      print a[i]
   i = i + 1
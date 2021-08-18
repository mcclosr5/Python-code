#!/usr/bin/env python

import sys

arg = sys.argv[1]
with open(arg, "r") as fd:
   s = fd.readlines()
i = 0
total = 0
while i < len(s):
   total = total + int(s[i])
   i = i + 1
print total

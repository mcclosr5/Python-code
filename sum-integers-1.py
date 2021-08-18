#!/usr/bin/env python

import sys

total = 0
line = sys.stdin.readlines()
i = 0
while i < len(line):
   total = total + int(line[i])
   i = i + 1
print total

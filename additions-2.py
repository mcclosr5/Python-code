#!/usr/bin/env python

import sys
s = sys.argv[1]

total = 0

start = 0
while start < len(s):
   end = start
   while end < len(s) and s[end] != "+":
      end = end  + 1
   total = total + int(s[start:end])
   start = end + 1

print total

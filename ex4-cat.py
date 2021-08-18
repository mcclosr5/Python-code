#!/usr/bin/env python
 
import sys
 
file_name = sys.argv[1]
 
i = 0
with open(file_name, "r") as fd:
   s = fd.readlines()
while i < len(s):
   lines = s[i]
   lines = lines.strip('\n')
   print lines
   i += 1
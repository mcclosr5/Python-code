#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s) and s[i] < "a" or "g" < s[i]:
   i = i + 1
if i < len(s):
   print s[i]

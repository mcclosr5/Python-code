#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
   if s[i] == ".":
      r = s[:i]
   elif s[i] == ".":
      m = s[i:]
   i = i + 1
print r, m

#!/usr/bin/env python

import sys

s = [1, 2]
i = 0
d = {
"1": True,
"2": True,
"3": True,
"4": True,
}
b = []
while i < len(s):
   word = s[i]
   if word in d:
      b.append(word)
   i = i + 1

for word in d:
   print b

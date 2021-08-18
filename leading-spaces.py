#!/usr/bin/env python

s = raw_input()

i = 0                               # Linear search.
while i < len(s) and s[i] == " ":   #
   i = i + 1                        #

print s[i:]

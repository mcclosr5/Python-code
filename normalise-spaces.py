#!/usr/bin/env python

t = ""
s = raw_input()

i = 0
while i < len(s):
   # Find the position of the next non-space.
   while i < len(s) and s[i] == " ":          # Linear search.
      i = i + 1                               #

   j = i
   if i < len(s):
      # We have found the position of the start of a word.
      # Find the position of the next space.
      while j < len(s) and s[j] != " ":       # Linear search again.
         j = j + 1                            #

      t = t + " " + s[i:j]

   i = j + 1

print t[1:]

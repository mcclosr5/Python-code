#!/usr/bin/env python
 
s = raw_input()
i = 0
count = 0
d = {
    "A"
    "B"
    "C"
    "D"
    "E"
    "F"
    "G"
    "H"
    "I"
    "J"
    "K"
    "L"
    "M"
    "N"
    "O"
    "P"
    "Q"
    "R"
    "S"
    "T"
    "U"
    "V"
    "W"
    "X"
    "Y"
    "Z"
   }
while i < len(s):
   if s[i] in d:
      count = count + 1
   i = i + 1
print count

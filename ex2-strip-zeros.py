#!/uasr/bin/env python

i = 0

s = "no"

while s!= "end":
   s = raw_input()
   if s != "end":
      while i < len(s) and s[i] == "0":
         i = i + 1
      if i < len(s):
         print s[i:]
      else:
         print 0
      i = 0

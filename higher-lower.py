#!/usr/bin/env python

new = 0
old = 0
i = 0
while i < 6:
   n = input()
   n = old
   if old < new:
      old = new
      print "lower"
   if old > new:
      old  = new
      print "higher"
   if new < old:
      print "lower"
   if new > old:
   	print "higher"
   else:
      old = new
      print "equal"
   i = i + 1

#!/usr/bin/env python

a = []
s = raw_input()
p = 0
j = 0
while s != "end":
   a.append(int(s))
   s = raw_input()

smallest = 0
i = input()
while i < len(a):
   if a[i] < a[smallest]:
      smallest = i
   i = i + 1
print smallest

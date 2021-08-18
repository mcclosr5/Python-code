#!/usr/bin/env python

a = [4, 3, 1, 2]
i = 0
j = i + 1
def swap(a, i, j):
   x = a[i]
   a[i] = a[j] 
   a[j] = x
   return a

def reverse(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1
      i = i + 1
   tmp = a[p]
   a[p] = a[i] 
   a[i] = tmp
   return a
if __name__ == "__main__":
   print swap(a,2,3)
   print reverse(a)

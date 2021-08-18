#!/usr/bin/env python

import sys

a = [4, 3, 2, 1]
def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < len(a) / 2:
   	   swap(a, i, len(a) - i - 1)
   	   i = i + 1
   return a
if __name__ == "__main__":
   print reverse(a)

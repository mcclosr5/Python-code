#!/usr/bin/env python

def selection_sort(a):
  i = 0
  while i < len(a):
     p = i
     j = i + 1
     while j < len(a):
        if a[j] < a[p]:            # Here.
           p = j
        j = j + 1

     # swap a[i] and a[p]
     tmp = a[p]
     a[p] = a[i]
     a[i] = tmp

     i = i + 1
print a

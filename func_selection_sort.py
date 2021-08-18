#!/usr/bin/env python

import func_selection_sort

a = [1, 3, 6, 2, 4, 2, 5, 2, 6]
def selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:            # Here.
            p = j
         j = j + 1

      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp

      i = i + 1
   return a

if __name__ == "__main__":
   print selection_sort(a)

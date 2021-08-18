#!/usr/bin/env python3

import sys

def swap_unique_keys_values(d):
   b = {}
   for n in d:
      if d[n] not in b:
         b[d[n]] = n
      else:
         b.pop(d[n])
   return b

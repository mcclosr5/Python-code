#!/usr/bin/env python

if __name__ == "__main__":
   a = ["", "", "dog", "cat", "mouse"]
 
i = 0
while i < len(a) and len(a[i]) == 0:
    i = i + 1
if i < len(a):
    print a[i]

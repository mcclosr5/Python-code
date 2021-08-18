#!/usr/bin/env python

def largest_position(a):
    i = 1
    j = 0
    while i < len(a):
        if a[i] > a[j]:
            j = i
        i += 1
    return j

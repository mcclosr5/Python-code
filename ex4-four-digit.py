#!/usr/bin/env python

import sys

s = sys.stdin.read().split()
i = 0
j = 0
while i < len(s):
    if len(s[i]) == 4:
        print int(s[i])
        i = i + len(s)
    i = i + 1

while j < len(s) and len(s[j]) != 4:
    j = j + 1
    if j == len(s):
        print 'none'
if len(s) == 0:
    print 'none'
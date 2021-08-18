#!/usr/bin/env python

import sys

s = sys.stdin.read().split()
i = 0
j = 0
while i < len(s):
    if int(s[i]) >= 100:
        print int(s[i])
        i = i + len(s)
    i = i + 1

while j < len(s) and int(s[j]) < 100:
    j = j + 1
    if j == len(s):
        print 'none'

#!/usr/bin/env python

with open("bar.txt") as fd:
   line = fd.readlines()

print line[0]

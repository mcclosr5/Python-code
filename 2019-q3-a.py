#!/usr/bin/env python

import sys
args = sys.argv[1:]

file1 = args[1]
file2 = args[1]

with open(file1) as f1:
   contents = f1.read()
   with open(file2, "w") as f2:
      f2.write(contents)

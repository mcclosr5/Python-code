#!/usr/bin/env python3

import sys

stud = sys.argv[1]
delin = sys.argv[2]

dict = {}

for line in open(stud):
    line = line.strip()
    dict[line] = 0

for line in open(delin):
    line = line.strip()
    if line in dict:

        dict[line] += 1

both = 0

for key, value in sorted(dict.items()):
    if value > 0:
        both += 1
        print('{}. {}'.format(both, key))

#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    d = {}
    lines = sys.stdin.read().split()
    for line in lines:
        total = lines.count(line)
        line = line.strip(punctuation).lower()
        if len(line) > 3 and line not in d:
            d[line] = 1
        elif len(line) > 3 and line in d:
            d[line] = d[line] + 1
        nd = {}
        for k in d:
            if 2 < d[k] and 3 < len(k):
                nd[k] = d[k]
    for k, v in sorted(nd.items()):
        maxkv = len(max(nd.keys(), key=len))
        if int(v) >= 3:
            print("{:>{:d}s} : {:{:d}d}".format(k, maxkv, v, 2))

if __name__ == '__main__':
    main()

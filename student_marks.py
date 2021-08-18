#!/usr/bin/env python3

import sys

def make_map():
    dic = {}
    s = sys.stdin.read().split('\n')
    for line in s:
        if len(line) > 0:
            stud, mark = line.strip().split()
            dic[stud] = mark
    return dic

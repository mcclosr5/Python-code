#!/usr/bin/env python3

import sys

def foo(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

def main():
    print(foo('apple')


if __name__ == '__main__':
    main()

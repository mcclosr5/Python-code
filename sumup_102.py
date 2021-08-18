#!/usr/bin/env python3

def factorial(n):

    if n == 0:
        return 0
    else:
        return n * sumup(n - 1)

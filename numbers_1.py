#!/usr/bin/env python3

def sum_to_k(lis, k):
    i = 0
    j = len(lis) - 1
    while i < j:
        if lis[i] + lis[j] == k:
            return True
        elif lis[i] + lis[j] < k:
            i += 1
        elif lis[i] + lis[j] > k:
            j -= 1
        return False

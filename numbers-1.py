#!/usr/bin/env python3

def sum_to_k(lis, k):
    i = 0
    j = 0
    while i < len(lis) - 1:
    	j = i + 1
        if j + i == k:
        	return True
        else:
        	return False

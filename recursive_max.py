#!/usr/bin/env python

def maximum(lis):
	if len(lis) == 1:
		return lis[0]
	return lis[0] if lis[0] >= maximum(lis[1:]) else maximum(lis[1:])
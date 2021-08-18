#!/usr/bin/env python

def get_counts(lis):
	counts = [0] * 10
	for w in lis:
		counts[len(w)] += 1
	return counts

#!/usr/bin/env python3

import sys

def get_counts_dict(list):
	dic = {}
	for word in list:
		if len(word) in dic:
			dic[len(word)] += 1
		else:
			dic[len(word)] = 1
	return dic

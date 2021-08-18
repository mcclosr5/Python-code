#!/usr/bin/env python3

from Queue import Queue

def print_queue(data, front, back):
	if back > front:
		return data[front:back]
	elif front > back:
		return data[front:] + data[:back]

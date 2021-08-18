#!/usr/bin/env python

def calc_average(numbers):
    sumlist = sum(numbers)
    average = sumlist / len(numbers)
    return average

def above_average(numbers):
    average = sum(numbers) / len(numbers)
    return [n for n in numbers if n > average]
            

#!/usr/bin/env python3

def maximum(list_of_numbers):
    #base case
    if len(list_of_numbers) == 1:
        return list_of_numbers[0]
    #recursive case
    head = list_of_numbers[0]
    maxtail = maximum(list_of_numbers[1:])
    # return the smaller of the two head, maxtail
    return head if head > maxtail else maxtail

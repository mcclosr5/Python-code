#!/usr/bin/env python3

def sumup(list_of_numbers):
    #base case
    if list_of_numbers == []:
        return 0
    return list_of_numbers[0] + sumup(list_of_numbers[1:])

x = sumup([5, 3, 1, 3])

print(x)

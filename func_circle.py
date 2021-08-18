#!/usr/bin/env python

pie = 3.141
def circumference(r):
   return 2 * (pie) * (r)
def area(r):
   return pie * (r ** 2)


if __name__ == "__main__":
   print circumference(2)
   print area(3)

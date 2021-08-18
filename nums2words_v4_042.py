#!/usr/bin/env python3

import sys

def main():
    d = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "one hundred"
    }
    for line in sys.stdin:
        lis = []
        tokens = line.strip().split()
        for num in tokens:
            if len(num) == 2 and int(num) > 19 and int(num) % 10 != 0:
                lis.append(d[int(num[0]) * 10] + "-" + d[int(num[1])])
            else:
                lis.append(d[int(num)])
        print(" ".join(lis))

if __name__ == '__main__':
    main()

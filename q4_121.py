#!/usr/bin/env python3

import sys

def camel_case_split(str):
    words = [[str[0]]]

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        elif words[-1][-1].isupper() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]
# Driver code
def main():
    for line in sys.stdin:
        line = ' '.join(camel_case_split(line.strip()))
        print(line.lower().capitalize())

if __name__ == '__main__':
    main()

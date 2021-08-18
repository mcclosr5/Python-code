#!/usr/bin/env python3

import sys

def main():

   best_student1 = ''
   best_students = []
   best_mark = 0
   lines = sys.argv[1]
   i = 0
   with open(lines, "r") as f:
      lines = f.readlines()
   for line in lines:
      tokens = line.strip().split()
      mark = int(tokens[0])
      name = ' '.join(tokens[1:])
      if mark > best_mark:
         best_mark = mark
         best_student1 = name
      elif mark == best_mark:
         best_students.append(name)

   print("Best student(s):", best_student1, best_students)
   print("Best mark:", best_mark)
if __name__ == '__main__':
    main()

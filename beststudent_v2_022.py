#!/usr/bin/env python3
 
import sys
 
def main():
   try:
      lines = sys.argv[1]
      i = 0
      bad = ""
      best_mark = 0
      best_student = ""
      with open(lines, "r") as f:
         lines = f.readlines()
         for line in lines:
            tokens = line.strip().split()
            num = int(tokens[0])
            name = ' '.join(tokens[1:])
            fake = tokens[0]
            if num > best_mark:
               best_mark = num
               best_student = name
            elif fake.isalpha():
               fake = bad
         print("Best student:", best_student)
         print("Best mark:", best_mark)
 
   except ValueError:
     print('Invalid mark {} encountered. Exiting.'.format(line.rstrip().split(" ", 1)[0]))
 
 
if __name__ == '__main__':
    main()

#!/usr/bin/env python

message = "pussy \n"
file_name = "bar.txt"

with open(file_name, "w") as fd:
   fd.write(message)

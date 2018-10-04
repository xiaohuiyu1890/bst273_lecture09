#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="oath to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

print("args = ", args)
print("args.data_file = ", args.data_file)

fh = open(args.data_file)
print("the file handle is", fh)

words=0
lines=0
chars=0

for line in fh:
    lines+=1

print(lines)


















#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------

######################
# Name: Darren Bowers
# Coding 08
# Purpose: Program to check line count, word count and character count then
# display a passed file.
######################

import sys
import os.path
import functions as fn

def main():
    argc = len(sys.argv)
    if argc==2:
        print("In", sys.argv[1], "there are", fn.count_lines(sys.argv[1]), "lines.")
        fn.dispay_file(sys.argv[1])
    else:
        print("You must pass in exactly one parameter.")

main()


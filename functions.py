######################
# Name: Darren Bowers
# Coding 08
# Purpose: Program to check line count, word count and character count then
# display a passed file.
######################

import sys
import os.path

def count_lines(filename):
    line_count = 0
    fin = open(sys.argv[1], 'r')
    for line in fin:
        line_count += 1
    return(line_count)

def count_words(line):
    # a line from the file is passed in
    # use any method you like to counts the words
    # assume one and only one space between words
    # assume no trailing or leading spaces
    # return the word count
    # hint: you can do it in one line of code
    # don't forget to erase the pass
    pass

def count_characters(line):
    # a line from the file is passed in
    # count the characters in the line USING A LOOP
    # assume anything not a space is a character
    # return the number of characters (not counting spaces)
    # don't forget to erase the pass
    pass
    
def dispay_file(filename):
    fin = open(sys.argv[1], 'r')
    text = 0
    line_count = 0
    for text in fin:
        text = text[:-1]
        line_count += 1
        print(" ", line_count,":", text)
    fin.close()
    
    # open the file
    # using the examples as your guide, make this function
    # display the file exactly as shown in the examples
    # you will need to call count_words() and count_characters()
    # return nothing
    # don't forget to erase the pass



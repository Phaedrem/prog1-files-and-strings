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
    words = line.split(' ')
    if words[0]=='':
        words.pop()
    return len(words)

def count_characters(line):
    characters = 0
    for i in line:
        characters += 1
        if i == " ":
            characters += -1
    return(characters)
    
def dispay_file(filename):
    fin = open(sys.argv[1], 'r')
    text = 0
    line_count = 0
    for text in fin:
        spaces = 0
        text = text[:-1]
        line_count += 1
        for i in range(len(text)):
                if text[i] == ' ':
                    spaces += 1
        if text == '':
            print(" ", line_count, ":", "[blank line]")
        else:
            print(" ", line_count,":", text, "[", count_words(text), "words,",
            count_characters(text), "characters,", spaces, "spaces ]")
    fin.close()

#
# your comment header here
#

import sys
import os.path
import functions as fn

def main():

    # these two lines are all you need to run the program, but they do not do error
    # checking to make sure the file exists before calling count_lines() and dispay_file()
    # fix it to do proper error checking as shown in the examples. then erase this comment.

    print("In", sys.argv[1], "there are", fn.count_lines(sys.argv[1]), "lines.")
    fn.dispay_file(sys.argv[1])

main()


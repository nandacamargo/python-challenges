'''This program returns True if a given year is a leap year; returns False if not'''

import sys
from getopt import getopt

def parser(argv):
    arg_input = ""
    arg_help = "{0} -f <input_file_name>".format(argv[0])
    
    try:
        opts, args = getopt(argv[1:], "f:", ["help", "filename="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-f", "--filename"):
            arg_input = arg
        
    return arg_input
    

def leap_year(year):
    if (year % 4 == 0 and year % 400 == 0):
        return True
    elif (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


if __name__ == '__main__':

    input_file = parser(sys.argv)
    print(input_file)
    
    with open(input_file, "r") as f:
        lines = f.readlines()

        for line in lines:
            year = int(line.strip())
            answer = leap_year(year)

            if answer:
                print(f"{year} is leap")
            else:
                print(f"{year} is not leap")


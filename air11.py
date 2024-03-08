import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or not is_num(arguments[1])):
    error_case()

#Return a pyramid with 2 args (heigth and symbol)
def make_pyramid(symbol, height):
    stringPyramid = ""
    spaces = (((height * 2) - 1) - 1) //2
    nbSymbols = 1

    while height != 0:
        stringPyramid += " " * spaces + symbol * nbSymbols + " " * spaces + "\n"
        spaces -= 1
        nbSymbols += 2
        height -= 1

    return stringPyramid
    
#Display results
symbol = arguments[0]
height = int(arguments[1])
print(make_pyramid(symbol, height))

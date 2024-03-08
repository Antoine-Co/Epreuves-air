import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 3)):
    error_case()

#Return a string with all args separated by a separator (Array -> string with separator)
def concat_separated(tabStrings, separator):
    stringRes = ""

    for eltString in tabStrings:
        stringRes += eltString + separator

    return stringRes

#Display results
separator = arguments.pop()
tabStrings = arguments
print(concat_separated(tabStrings, separator))

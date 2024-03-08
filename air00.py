import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1) or is_num(arguments[0])):
    error_case()

#Return an array with each string separated
def separate_string(stringComplete):
    tab = []
    indexTmp = 0

    for i in range(len(stringComplete) - 1):
        if (stringComplete[i] == ' ' or stringComplete[i] == '\n' or stringComplete[i] == '\t'): #If the separator is located
            tab.append(stringComplete[indexTmp:i])
            indexTmp = i + 1
        elif (i == len(stringComplete) - 2): #If we are at the end of the string
            tab.append(stringComplete[indexTmp:])

    return tab

#Display results
stringASeparer = arguments[0]
print_list_by_line(separate_string(stringASeparer))

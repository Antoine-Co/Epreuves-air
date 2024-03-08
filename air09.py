import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 2)):
    error_case()

#Return a list shifted to the left
def shift_list(listArgs):
    firstArg = listArgs[0]

    for i in range(1,len(listArgs)):
        listArgs[i - 1] = listArgs[i]

    #replace last elt by the first
    listArgs[-1] = firstArg

    return listArgs

#Display results
print_list_to_string(shift_list(arguments))

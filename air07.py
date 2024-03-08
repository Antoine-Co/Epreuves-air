import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 3) or is_args_all_alpha(arguments)):
    error_case()

#Return the array sorted with the new element
def sorted_insert(arraySorted, newElt):
    arraySorted = convert_array_to_int(arraySorted)
    newArraySorted = []

    for i in range(len(arraySorted)):
        if (arraySorted[i] >= newElt and arraySorted[i - 1] <= newElt):
            newArraySorted.append(newElt)
            newArraySorted.append(arraySorted[i])
        else:
            newArraySorted.append(arraySorted[i])

    return newArraySorted

#Conversion from string array to int array
def convert_array_to_int(stringArray):
    tabInt = []

    for stringValue in stringArray:
        tabInt.append(int(stringValue))

    return tabInt

#Display results
newElt = int(arguments.pop())
arraySorted = arguments
print_list_to_string(sorted_insert(arraySorted, newElt))

import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 3) or is_args_all_alpha(arguments)):
    error_case()

#Return the sorted fusion of 2 list
def sorted_fusion(sortedList1, sorted_list2):
    arrayFusion = []
    i, j = 0, 0

    while i < len(sortedList1) and j < len(sortedList2):
        if (sortedList1[i] < sortedList2[j]):
            arrayFusion.append(sortedList1[i])
            i += 1
        else:
            arrayFusion.append(sortedList2[j])
            j += 1

    #We add the lasts elements
    arrayFusion.extend(sortedList1[i:])
    arrayFusion.extend(sortedList2[j:])

    return arrayFusion

#Get the sorted list in args
sortedList1 = []
sortedList2 = []

for i in range(len(arguments) -1):
    if (arguments[i] == "fusion"):
        sortedList1 = arguments[:i]
        sortedList2 = arguments[i+1:]
        break

#Display results
print_list_to_string(sorted_fusion(sortedList1, sortedList2))

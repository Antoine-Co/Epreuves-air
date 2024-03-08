import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 3)):
    error_case()

#Return the value with no pair inside a list
def no_pair_in_list(listArgs):
    tabRes = []

    for element in listArgs: #Iterate on each arguments
        if(not is_in_list(element, list_without(listArgs, element))):
            tabRes.append(element)

    return tabRes

#Return an array without an element
def list_without(listArgs, elementToDelete):
    listRes = []
    flag = 0

    for element in listArgs:
        if (element == elementToDelete and flag == 1): #Only the first occurence
            listRes.append(element)
        elif(element != elementToDelete):
            listRes.append(element)
        else:
            flag = 1

    return listRes

#Return True if an element is in the list
def is_in_list(eltToFind, list):
    for elt in list:
        if (eltToFind == elt):
            return True
    return False

#Display results
print_list_to_string(no_pair_in_list(arguments))

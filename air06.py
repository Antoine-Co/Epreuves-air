import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 2) or not is_alpha(arguments[0])):
    error_case()

#Return array whith strings without the char inside 
def delete_strings_with_substr(tabStrings, charToDel):
    tabRes = []

    for string in tabStrings:
        if(not is_in_string(charToDel, string)):
            tabRes.append(string)

    return tabRes

#Return True if an element is in the string
def is_in_string(eltToFind, string):
    for elt in string:
        elt = elt.lower()   #Condition to compare
        eltToFind = eltToFind.lower()
        if (eltToFind == elt):
            return True
    return False

#Display results
charToDel = arguments.pop()
tabStrings = arguments
print_list_to_string(delete_strings_with_substr(tabStrings, charToDel))

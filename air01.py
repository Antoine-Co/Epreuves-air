import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or is_num(arguments[0]) or is_num(arguments[1])):
    error_case()

#Return an array with each string separated
def separate_string_by_separator(stringComplete, separator):
    tab = []
    indexTmp = 0

    for i in range(len(stringComplete)):
        if (stringComplete[i:i+len(separator)] == separator): #Separator found
            tab.append(stringComplete[indexTmp:i])            #Add the begining to the index wanted
            indexTmp = i + len(separator)
            while(not is_alpha(stringComplete[indexTmp])):    #To avoid spaces in the strings in the array
                indexTmp += 1
        elif(i == len(stringComplete) - 2):                   #To add the end of the string
            tab.append(stringComplete[indexTmp:])

    return tab

#Display results
stringASeparer = arguments[0]
separator = arguments[1]
print_list_by_line(separate_string_by_separator(stringASeparer, separator))

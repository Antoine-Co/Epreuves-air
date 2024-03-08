import sys, os
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 1) or not os.path.exists(arguments[0])):
    error_case()

#Return the content of a file
def read_file(nameFile):
    file = open(nameFile)
    stringRes = file.read()
    return stringRes

#Display results
print(read_file(arguments[0]))

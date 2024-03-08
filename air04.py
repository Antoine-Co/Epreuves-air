import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1)):
    error_case()

#Return a string without 2 char repeated
def string_without_repetition(stringToAnalyse):
    stringRes = ""

    for i in range(len(stringToAnalyse)):
        if (i < len(stringToAnalyse) - 1 and stringToAnalyse[i] != stringToAnalyse[i + 1]): #Stop condition + no repetition
            stringRes += stringToAnalyse[i]
        elif (stringToAnalyse[i] == stringToAnalyse[i - 1]): #To keep one char of the repeated char
            stringRes += stringToAnalyse[i]

    return stringRes

#Display results
print(string_without_repetition(arguments[0]))

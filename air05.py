import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 2) or not is_num(arguments[-1][1]) or not len(arguments[-1]) == 2):
    error_case()

#Return the list more the operation done on each element
def operation_list(listNumbers, operation):
    number = int(operation[1])
    operand = operation[0]

    for i in range(len(listNumbers)):
        if (operand == "-"):
            listNumbers[i] -= number
        elif(operand == "+"):
            listNumbers[i] += number
        elif(operand == "*"):
            listNumbers[i] *= number
        elif(operand == "/"):
            listNumbers[i] /= number

    return listNumbers

#Conversion from string array to int array
def convert_array_to_int(stringArray):
    tabInt = []

    for stringValue in stringArray:
        tabInt.append(int(stringValue))

    return tabInt

#Display results
operation = arguments.pop()
listNumbers = convert_array_to_int(arguments)

print_list_to_string(operation_list(listNumbers, operation))

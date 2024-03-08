import sys, random
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 3) or not is_args_all_num(arguments)):
    error_case()

#Return a sorted list with quicksort algo
def quick_sort(liste, debut, fin):
    if debut < fin:
        indice_partition = partition(liste, debut, fin)

        quick_sort(liste, debut, indice_partition - 1)
        quick_sort(liste, indice_partition + 1, fin)

#Return the index of the partition 
def partition(liste, debut, fin):
    pivot = liste[fin]
    i = debut - 1

    for j in range(debut, fin):
        if liste[j] <= pivot:
            i += 1
            liste[i], liste[j] = liste[j], liste[i]

    liste[i + 1], liste[fin] = liste[fin], liste[i + 1]
    return i + 1

#Conversion from string array to int array
def convert_array_to_int(stringArray):
    tabInt = []

    for stringValue in stringArray:
        tabInt.append(int(stringValue))

    return tabInt

#Display results
arrayInt = convert_array_to_int(arguments)
firstInt = 0
lastInt = len(arrayInt) - 1

quick_sort(arrayInt, firstInt, lastInt)
print(arrayInt)

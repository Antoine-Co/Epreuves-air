import sys, os
from fonctions_annexes import *
import subprocess

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 0)):
    error_case()

#Return True if the exo1 exist and is correct
def test():
    nbTestTotalOK = 0

    for i in range(0,13):
        #Forming the function name and the filename
        nb_exo = get_index_on_two_digits(i)
        current_file = "air" + nb_exo + ".py"
        nomFunction = "test_exo" + str(i)

        #To get the nb test passed results of the function executed
        locRes = {}
        exec(f"nbTests = {nomFunction}('{current_file}')",None,locRes)
        nbTestTotalOK += locRes['nbTests']

    print("Total de tests validés " + str(nbTestTotalOK) + "/27")

#Return number tests passed for each exo
def test_exo0(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Bonjour ca va mec"])

    if (output_command == b'Bonjour\nca\nva\nmec\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo1(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Bonjour ca va mec", "ca"])

    if (output_command == b'Bonjour \nva mec\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo2(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Bonjour", "je", "test", " "])

    if (output_command == b'Bonjour je test \n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo3(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/3) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/3) : failure")

    output_command = subprocess.check_output(["python3", file, "1", "2" ,"3" ,"4" ,"5" ,"4", "3", "2" ,"1"])

    if (output_command == b'5\n'):
        print(file, "(2/3) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/3) : failure")

    output_command = subprocess.check_output(["python3", file, "bonjour", "monsieur" ,"bonjour"])

    if (output_command == b'monsieur\n'):
        print(file, "(2/3) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/3) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo4(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Yo bbien ou  bien "])

    if (output_command == b'Yo bien ou bien\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo5(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "1", "2", "3", "4", "5", "6", "*5"])

    if (output_command == b'5, 10, 15, 20, 25, 30\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo6(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Michel", "Albert", "Thérèse", "Benoit", "t"])

    if (output_command == b'Michel\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo7(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "1", "3", "4", "2"])

    if (output_command == b'1, 2, 3, 4\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo8(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "10", "20", "30", "fusion", "15", "25", "35"])

    if (output_command == b'10, 15, 20, 25, 30, 35\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo9(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "Michel", "Albert", "Thérèse", "Benoit"])

    if (output_command == b'Albert, Th\xc3\xa9r\xc3\xa8se, Benoit, Michel\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo10(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "a.txt"])

    if (output_command == b'Je danse la swagance\n\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return number tests passed for each exo
def test_exo11(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "o", "5"])

    if (output_command == b'    o    \n   ooo   \n  ooooo  \n ooooooo \nooooooooo\n\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

def test_exo12(file):
    nbTestPassed = 0
    if (os.path.exists(file)):
        print(file, " (1/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(1/2) : failure")

    output_command = subprocess.check_output(["python3", file, "6", "5", "4", "3", "2", "1"])

    if (output_command == b'[1, 2, 3, 4, 5, 6]\n'):
        print(file, "(2/2) : success")
        nbTestPassed += 1
    else:
        print(file, "(2/2) : failure")

    return nbTestPassed

#Return an index on 2 digits
def get_index_on_two_digits(index):
    if (index < 10):
        return "0" + str(index)
    else:
        return str(index)

test()

#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Calculator**
# A simple calculator to do basic operators. Make it a scientific calculator
# for added complexity.

def get_number_of_calculations():
    return int(raw_input("Please enter the number of calculations you would like to perform (1-9):\n"))

def display_calculation_header(calc):
    print "Calcuation ", calc + 1

def get_operation():
    operation = {}
    operation["operands"] = ["operand1", "operand2"]
    op = raw_input("Please enter one of the following operation 'add', 'sub', 'mul', 'div':\n")
    operation['calc'] = dict(zip(['add', 'sub', 'mul', 'div'],
                                [lambda x, y: (x + y, "{x} + {y} =".format(x = x, y = y)),
                                 lambda x, y: (x - y, "{x} - {y} =".format(x = x, y = y)),
                                 lambda x, y: (x * y, "{x} * {y} =".format(x = x, y = y)),
                                 lambda x, y: (x / y, "{x} / {y} =".format(x = x, y = y))]
                                )
                            )[op]
    return operation

def get_operands(operation):
    for operand in operation["operands"]:
        operation[operand] = int(raw_input("Please enter " + operand + ":\n"))

def display_result_of_calculation(operation, calc):
    operation["result"], operation["disp"] = operation["calc"](operation["operand1"], operation["operand2"])
    print "The result of calculation {calc}: {disp} {result}".format(calc = calc + 1,
                                                                     result = operation["result"],
                                                                     disp = operation["disp"])

def ask_to_continue():
    reply = raw_input("Do you wish to continue?[Y/N]:\n")
    while reply.upper() not in ["Y", "N"]:
        reply = raw_input("Please enter Y or N:\n")
    if reply.upper() == "Y":
        return True
    else:
        return False

def main():
    cont = True
    operation = None
    while cont:
        calcs = get_number_of_calculations()
        for calc in range(calcs):
            display_calculation_header(calc)
            operation = get_operation()
            get_operands(operation)
            display_result_of_calculation(operation, calc)
        cont = ask_to_continue()

if __name__ == '__main__':
  main()

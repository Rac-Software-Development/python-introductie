def debug_print(first_number, second_number, operator_type):
    if first_number == 0:
        print('Debug: first_number is 0')
    if second_number == 0:
        print('Debug: second_number is 0')
    print(f"Debug: {first_number} {operator_type} {second_number}")

def add(first_number, second_number, debug=False):
    if debug:
        debug_print(first_number, second_number, '+')
    print(first_number + second_number)

def subtract(first_number, second_number, debug=False):
    if debug:
        debug_print(first_number, second_number, '-')
    print(first_number - second_number)

def multiply(first_number, second_number, debug=False):
    if debug:
        debug_print(first_number, second_number, '*')
    print(first_number * second_number)

def divide(first_number, second_number, debug=False):
    if debug:
        debug_print(first_number, second_number, '/')
    print(first_number / second_number)

def calculate(first_number, second_number, operator_type, debuginput):
    if debuginput == 'Yes':
        debug = True
    else:
        debug = False

    if operator_type == '+':
        add(first_number, second_number, debug)
    elif operator_type == '-':
        subtract(first_number, second_number, debug)
    elif operator_type == '*':
        multiply(first_number, second_number, debug)
    elif operator_type == '/':
        divide(first_number, second_number, debug)
    else:
        print('Abort, unknown input.')

input1 = input('Geef het eerste getal: ')
input2 = input('Geef het tweede getal: ')
inputdebug = input('Debug? [Yes/No]: ')
operator = input('Geef de operator (+, -, * of /): ')
calculate(int(input1), int(input2), operator, inputdebug)




def add(first_number, second_number):
    print(first_number + second_number)

def subtract(first_number, second_number):
    print(first_number - second_number)

def multiply(first_number, second_number):
    print(first_number * second_number)

def divide(first_number, second_number):
    print(first_number / second_number)

def calculate(first_number, second_number, operator):
    if operator == '+':
        add(first_number, second_number)
    elif operator == '-':
        subtract(first_number, second_number)
    elif operator == '*':
        multiply(first_number, second_number)
    elif operator == '/':
        divide(first_number, second_number)
    else:
        print('Abort, unknown input.')

input1 = input('Geef het eerste getal: ')
input2 = input('Geef het tweede getal: ')
operator = input('Geef de operator (+, -, * of /): ')
calculate(int(input1), int(input2), operator)




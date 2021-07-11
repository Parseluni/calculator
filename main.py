def calculator():

    print("calculator is on")

    num1_input = input("Please enter first number: ")
    operation = input("Please enter operation: ")
    num2_input = input("Please enter second number: ")

    if not num1_input.isnumeric() or not num2_input.isnumeric():
        return "Please enter a valid number"
    else:
        num1 = int(num1_input)
        num2 = int(num2_input)

    if operation == 'addition' or operation == 'plus' or operation == '+':
        return addition(num1, num2)
    elif operation == 'subtraction' or operation == 'minus' or operation == '-':
        return subtraction(num1, num2)
    elif operation == 'multiplication' or operation == 'times' or operation == '*':
        return multiplication(num1, num2)
    elif operation == 'division' or operation == 'divided by' or operation == '/':
        return division(num1, num2)
    else:
        return "Invalid choice"

def addition(num1, num2):
    return (num1 + num2)

def subtraction(num1, num2):
    return (num1 - num2)

def multiplication(num1, num2):
    return (num1 * num2)

def division(num1, num2):
    result = round((num1 / num2), 2)
    return result

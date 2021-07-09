
def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    return(num1 / num2)

def calculator(num1, num2, operation):
    if operation == add:
        return add(num1, num2)
    elif operation == subtract:
        return subtract(num1, num2)
    elif operation == multiply:
        return multiply(num1, num2)
    elif operation == divide:
        return divide(num1, num2)
    else:
        return "Invalid choice"

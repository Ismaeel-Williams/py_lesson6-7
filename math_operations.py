def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

import random
import math_operations
#Question1
fruits = ["apple", "watermelon", "avocado", "cucumber", "grapes", "orange"]
for fruit in fruits:
    print(fruit)

#Question2
n = 5
while n > 0:
    print(n)
    n -= 1 

#Question3
for i in range(1, 11):
    print(i**2)

#Question4
Colors = ["red", "blue", "purple", "pink","yellow","cyan"]
for i in range(3):
    print(random.choice(Colors))

#Question5
input("Enter 1 for calculator or 2 to skip: ")
while input == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, %, **): ")
    if operation == "+":
        print(math_operations.add(num1, num2))
    elif operation == "-":
        print(math_operations.subtract(num1, num2))
    elif operation == "*":
        print(math_operations.multiply(num1, num2))
    elif operation == "/":
        print(math_operations.divide(num1, num2))
    elif operation == "%":
        print(math_operations.modulo(num1, num2))
    elif operation == "**":
        print(math_operations.power(num1, num2))

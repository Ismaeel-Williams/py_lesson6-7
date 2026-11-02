from math_operations import add, subtract, multiply, divide, modulo, power
import random

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
choice = input("Enter 1 for calculator or 2 to skip: ").strip()
while choice == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, %, **): ")
    if operation == "+":
        print(add(num1, num2))
    elif operation == "-":
        print(subtract(num1, num2))
    elif operation == "*":
        print(multiply(num1, num2))
    elif operation == "/":
        print(divide(num1, num2))
    elif operation == "%":
        print(modulo(num1, num2))
    elif operation == "**":
        print(power(num1, num2))
    else:
        print("Invalid operation")
    choice = input("Enter 1 to calculate again or 2 to skip: ").strip()

import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter operation (+, -, *, /, log): ").strip().lower()

if operation == "+":
    print("result:", num1 + num2)

elif operation == "-":
    print("result:", num1 - num2)

elif operation == "*":
    print("result:", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("result:", num1 / num2)

elif operation == "log":
    if num1 <= 0 or num2 <= 0 or num2 == 1:
        print("For log, the first number must be > 0 and the second number must be > 0 and not equal to 1")
    else:
        print("result:", math.log(num1, num2))

else:
    print("Invalid operation entered")

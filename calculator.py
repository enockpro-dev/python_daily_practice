num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter operation:" )

if operation == "+":
    print("result:", num1 + num2)

elif operation == "-":
    print("result:", num1 - num2)

elif operation == "*":
    print("result:", num1 * num2)
elif operation == "/":
    print("result:", num1 / num2)

else:
    print("Invalid operation entered")

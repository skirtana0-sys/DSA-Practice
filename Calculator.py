a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result of Addition=", a + b)
elif op == "-":
    print("Result of Subtraction=", a - b)
elif op == "*":
    print("Result of Multiplication=", a * b)
elif op == "/":
    print("Result of Division=", a / b)
else:
    print("Invalid Operator")

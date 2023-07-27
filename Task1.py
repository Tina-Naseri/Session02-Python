import math

print("Welcome to the Calculator!")
op = input("Enter Your Operation(+, -, *, /, sin, cos, tan, cot, factorial. radical):")

if op == "sin":
    angle = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle)
    result = math.sin(angle_radians)
    print("The sin of", angle, "degrees is", round(result, 2))

if op == "cos":
    angle = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle)
    result = math.cos(angle_radians)
    print("The cos of", angle, "degrees is", round(result, 2))

if op == "tan":
    angle = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle)
    result = math.tan(angle_radians)
    if result == 1.633123935319537e+16:
        print ("The tan of", angle, "degrees is","∞")
    else:
        print("The tan of", angle, "degrees is", round(result, 2))

if op == "cot":
    angle = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle)
    result = 1 / math.tan(angle_radians)
    if result == 1.633123935319537e+16:
        print ("The can of", angle, "degrees is","∞")
    else:
        print("The cot of", angle, "degrees is", round(result, 2))

if op == "factorial":
    nF = int(input("Enter a non-negative number: "))
    if nF < 0:
        print("Error: Input must be (NON-NEGATIVE)")
    if nF == 0:
        print("The factorial of", nF, "is 1")
    else:
        result = math.factorial(nF)
        print("The factorial of number", int(nF), "is: ", result)

if op == "radical":
    nR = float(input("Enter a non-negative number: "))
    if nR < 0:
        print("Error: Input must be (NON-NEGATIVE)")
    else:
        result = math.sqrt(nR)
        print("The square root of", nR, "is", result)

if op == "+":
    num1 = int(input("Enter Number 1: "))
    num2 = int (input("Enter Number 2: "))
    result = num1 + num2
    print(num1, "+", num2, "=", result)

if op == "-":
    num1 = int(input("Enter Number 1: "))
    num2 = int (input("Enter Number 2: "))
    result = num1 - num2
    print(num1, "-", num2, "=", result)

if op == "*":
    num1 = int(input("Enter Number 1: "))
    num2 = int (input("Enter Number 2: "))
    result = num1 * num2
    print(num1, "*", num2, "=", result)

if op == "/":
    num1 = int(input("Enter Number 1: "))
    num2 = int (input("Enter Number 2: "))
    if num2 == 0:
        print("Error: The Number 2 must be (NON-ZERO)")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)

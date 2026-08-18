from loguru import logger

num1 = float(input("Enter first number: "))
print(num1)
while True:
    operator1 = input("Select operator of your choice (+,-,/,*) or '=' to end the session ")

    if operator1 == "=":
        print("Operator is equal to '='")
        print(num1)
        break

    if operator1 not in ["+", "-", "*", "/"]:
        print("enter valid operator")
        continue

    num2 = float(input("Enter second number: "))

    if operator1 == "+":
        num1 = num1 + num2
    elif operator1 == "-":
        num1 = num1 - num2
    elif operator1 == "*":
        num1 = num1 * num2
    elif operator1 == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            continue
        num1 = num1 / num2

    print("Result:", num1)




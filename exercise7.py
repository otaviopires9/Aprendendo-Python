# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"{round(result ,2)}")
elif operator == "*":
    result = num1 * num2
    print(f"{round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"{round(result, 2)}")
else:
    print(f"{operator} is not valid operator")
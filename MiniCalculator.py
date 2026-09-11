print("====== Mini Calculator ======")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Choose operation: + - * / % ")

if operator == "+":
    print("Addition:", num1 + num2)

elif operator == "-":
    print("Subtraction:", num1 - num2)

elif operator == "*":
    print("Product:", num1 * num2)

elif operator == "/":
    print("Division:", num1 / num2)

elif operator == "%":
    print("Remainder:", num1 % num2)

else:
    print("Enter a valid operator!")

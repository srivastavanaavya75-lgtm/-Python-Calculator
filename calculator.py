def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


print("===== Simple Calculator =====")
print("Operations: +  -  *  /")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator!"

        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    choice = input("\nDo you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed.")
        break

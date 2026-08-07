# Abhishek_jadhav_69137
# Assignment_4  

print("FUNCTION CALCULATOR")

# Addition 
def addition(num1, num2):
    result = num1 + num2
    return result

# Subtraction 
def subtraction(num1, num2):
    result = num1 - num2
    return result

# Multiplication 
def multiplication(num1, num2):
    result = num1 * num2
    return result

# Division 
def division(num1, num2):
    result = num1 / num2
    return result

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter Choice:")

    if choice == "1":

        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        result = addition(num1, num2)
        print("Result =", result)

    elif choice == "2":

        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        result = subtraction(num1, num2)
        print("Result =", result)

    elif choice == "3":

        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        result = multiplication(num1, num2)
        print("Result =", result)

    elif choice == "4":

        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = division(num1, num2)
            print("Result =", result)

    elif choice == "5":

        print("Calculator Closed")
        break

    else:

        print("Invalid Choice")
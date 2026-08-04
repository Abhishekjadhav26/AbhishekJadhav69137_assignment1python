# Abhishek_jadhav_69137
# Assingnment_1

print("===== CALCULATOR =====");

print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");

choice = input("Enter your choice (1-4):");

if choice == "1":
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    result = number1 + number2;
    print(f"The result is: {result}");

elif choice == "2":
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    result = number1 - number2;
    print(f"The result is: {result}");

elif choice == "3":
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    result = number1 * number2;
    print(f"The result is: {result}");

elif choice == "4":
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    if number2 != 0:
        result = number1 / number2;
        print(f"The result is: {result}");
    else:
        print("Division by zero is not possible");

else:
    print("Invalid choice");
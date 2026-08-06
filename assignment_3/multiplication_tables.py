# # Abhishek_jadhav_69137
# # Assignment_3


print("MULTIPLICATION TABLE");
# Keep displaying the menu until the user chooses to exit  (additional)
while True:
    print("\n1. Generate Multiplication Table");
    print("4. Exit");

    choice = input("Enter your choice:");

    if choice == "1":
        number = int(input("Enter a number:"));
        start = int(input("Enter starting multiplier:"));
        end = int(input("Enter ending multiplier:"));

        if start <= end:
            for multiplier in range(start, end + 1):
                result = number * multiplier;
                print(f"{number} x {multiplier} = {result}");
        else:
            print("Starting multiplier cannot be greater than ending multiplier.");

     # Exit the program when the user enters 4 (additional)
    elif choice == "4":
        print("Program exited.");
        break;

    else:
        print("Invalid choice! Please select 1 or 4.");
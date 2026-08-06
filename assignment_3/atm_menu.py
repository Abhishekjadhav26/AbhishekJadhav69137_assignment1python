# Abhishek_jadhav_69137
# Assignment_3  

print("SIMPLE ATM BANKING SYSTEM");
balance = 10000;

while True:
    print("\nATM MENU");
    print("1. Check Balance");
    print("2. Deposit Money");
    print("3. Withdraw Money");
    print("4. Exit");

    choice = input("Enter your choice:");

    if choice == "1":
        print(f"Current balance: ₹{balance}");

    elif choice == "2":
        deposit_amount = int(input("Enter deposit amount:"));

        if deposit_amount > 0:
            balance += deposit_amount;
            print("Money deposited successfully.");
            print(f"Updated balance: ₹{balance}");
        else:
            print("Deposit amount must be greater than zero.");

    elif choice == "3":
        withdrawal_amount = int(input("Enter withdrawal amount:"));

        if withdrawal_amount <= 0:
            print("Withdrawal amount must be greater than zero.");
        elif withdrawal_amount > balance:
            print("Insufficient balance.");
        else:
            balance -= withdrawal_amount;
            print("Money withdrawn successfully.");
            print(f"Updated balance: ₹{balance}");

    elif choice == "4":
        print("Thank you for using the ATM.");
        break;

    else:
        print("Invalid choice Please select an option from 1 to 4.");
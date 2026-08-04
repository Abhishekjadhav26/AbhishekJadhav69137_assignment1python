# Abhishek_jadhav_69137
# Assignment_2


print("===== CURRENCY CONVERTER =====");

print("1. Dollar to Rupees");
print("2. Rupees to Dollar");

choice = input("Enter your choice (1 or 2):");

exchange_rate = 83.00;

if choice == "1":
    dollar = float(input("Enter amount in Dollar:"));

    rupees = dollar * exchange_rate;

    print(f"${dollar} = ₹{rupees:.2f}");

elif choice == "2":
    rupees = float(input("Enter amount in Rupees:"));

    dollar = rupees / exchange_rate;

    print(f"₹{rupees} = ${dollar:.2f}");

else:
    print("Invalid choice!");
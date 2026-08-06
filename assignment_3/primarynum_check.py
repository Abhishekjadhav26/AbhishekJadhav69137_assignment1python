# Abhishek_jadhav_69137
# Assignment_3

print("PRIME NUMBER CHECKER");

number = int(input("Enter a positive integer:"));
factor = 0;

if number <= 1:
    print(f"{number} is Not Prime.");
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            factor = divisor;
            break;

    if factor == 0:
        print(f"{number} is Prime.");
    else:
        print(f"{number} is Not Prime.");
        print(f"{factor} is a factor of {number}.");
# Abhishek_jadhav_69137
# Assignment_2

print("===== AREA CALCULATOR =====");

print("1. Rectangle");
print("2. Circle");
print("3. Triangle");

choice = input("Enter your choice (1-3):");

if choice == "1":
    length = float(input("Enter the length of the rectangle:"));
    width = float(input("Enter the width of the rectangle:"));

    area = length * width;

    print(f"The area of the rectangle is: {area}");

elif choice == "2":
    radius = float(input("Enter the radius of the circle:"));

    area = 3.14 * radius * radius;

    print(f"The area of the circle is: {area}");

elif choice == "3":
    base = float(input("Enter the base of the triangle:"));
    height = float(input("Enter the height of the triangle:"));

    area = 0.5 * base * height;

    print(f"The area of the triangle is: {area}");

else:
    print("Invalid choice!");
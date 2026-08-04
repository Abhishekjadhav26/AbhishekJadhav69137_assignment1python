# Abhishek_jadhav_69137
# Assignment_2

print("===== EMPLOYEE SALARY CALCULATOR =====");

employee_name = input("Enter employee name:");
basic_salary = int(input("Enter basic salary:"));
bonus = int(input("Enter bonus amount:"));

total_salary = basic_salary + bonus;

if total_salary >= 100000:
    high_earner = True;
else:
    high_earner = False;

print("\n----- Employee Summary -----");
print(f"Employee Name : {employee_name}");
print(f"Basic Salary : {basic_salary}");
print(f"Bonus : {bonus}");
print(f"Total Salary : {total_salary}");
print(f"High Earner : {high_earner}");
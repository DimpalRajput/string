# Student Information System

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
student_class = input("Enter Class: ")
age = int(input("Enter Age: "))

print("\n----- STUDENT DETAILS -----")
print("Name :", name)
print("Roll Number :", roll)
print("Class :", student_class)
print("Age :", age)
# Basic Calculator

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nRESULTS")
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)
    print("Modulus =", num1 % num2)
else:
    print("Division cannot be performed because second number is 0.")

print("Power =", num1 ** num2)
# Area and Perimeter of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("\nRectangle Details")
print("Area =", area)
print("Perimeter =", perimeter)
# Temperature Converter

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (9/5 * c) + 32
    print("Temperature in Fahrenheit =", f)

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius =", c)

else:
    print("Invalid Choice")
    # Largest and Smallest Number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

largest = max(a, b, c)
smallest = min(a, b, c)

print("Largest Number =", largest)
print("Smallest Number =", smallest)
# Leap Year Checker

year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
  # Voting Eligibility

name = input("Enter Name: ")
age = int(input("Enter Age: "))

if age >= 18:
    print(name, "is eligible to vote.")
else:
    print(name, "is not eligible to vote.")
    print("You can vote after",18-age,"year(s).")
# Multiplication Table

num = int(input("Enter Number: "))

print("\nTable of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
 # Sum from 1 to N

n = int(input("Enter a Number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
       

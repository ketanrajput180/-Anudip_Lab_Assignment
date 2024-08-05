 #Q1 Program to check if a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q2 Program to check if a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Q3 Program to check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Q4 Program to check if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Q5 Program to find the largest of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")



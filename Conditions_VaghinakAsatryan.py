#1. Write a Python program that accepts a word from the user and reverse it.

word = input("Input a word to reverse: ")

print(word[::-1])

print("________________________________________________________________________________________")

#2. Write a Python program to count that user inputed number is even or odd.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

#3. Write a Python program to find the inputed number from 100 to 400 (both included).


print("________________________________________________________________________________________")

number = int(input("Enter a number: "))
if number >= 100 and number <= 400:
    print(True)
else:
    print(False)

print("________________________________________________________________________________________")
#4. Write a Python program that get 2 numbers from user and retur Biggest, Median, Sum, Multiply, Divide and Subtract


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print(num1, "greater than", num2)
elif num1 == num2:
    print(num1, "equals to", num2)
else:
    print(num2, "greater than", num1)



med = (num1 + num2) / 2
print("Median of", num1, "and", num2, "is", med)

print("Enter which operation would you like to perform?")
operation = input("Enter any of these char for specific operation +,-,*,/: ")

result = "Input character is not recognized!"

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2

elif operation == '/':
    result = num1 / num2

else:
    print("Input character is not recognized!")


print(num1, operation , num2, "=", result)

print("________________________________________________________________________________________")

#5. Write a Python program to get next day of a given date.
	#Expected Output:

	#Input a year: 2016
	#Input a month [1-12]: 8
	#Input a day [1-31]: 23
	#The next date is [yyyy-mm-dd] 2016-8-24


year = int(input("Input a year: "))

if (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
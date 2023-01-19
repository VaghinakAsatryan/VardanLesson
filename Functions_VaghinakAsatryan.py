# 1. Write a function to multiply all the numbers in a given list

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply([8, 2, 1, 7]))

print("_____________________________________________________")
# 2. Write a function that takes a list and returns a new list with unique elements of the first list

myList = [1, 1, 2, 2, 3, 3, 4, 6, 5, 4, 8, 61, 61, 85]
def add(simon):

    return list(set(simon))

x = add(myList)
print(x)

print("__________________________________________________")
# 3. Write a function to print the even numbers from a given list.

def even(numbers):
    evenNumber = []
    for x in numbers:
        if x % 2 == 0:
            evenNumber.append(x)
    return evenNumber
print(even([8, 2, 1, 7, 6, 4, 7, 9]))

print("_____________________________________________________")
    # 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
    #  Sample String : 'The quick Brow Fox'
    # Expected Output :
    #  No. of Upper case characters : 3
    #  No. of Lower case Characters : 12

def show_upper_and_lower(text):
    uppercaseCount = 0
    lowercaseCount = 0
    for i in text:
        if i.isupper():
            uppercaseCount += 1
        elif i.islower():
            lowercaseCount += 1
        else:
            pass
    print("Original text is:", text)
    print("Uppercases count is:", uppercaseCount)
    print("Lowercases count is:", lowercaseCount)

show_upper_and_lower("Hello World")

print("_______________________________________________________")
    # 5. Write a Python function that takes a number as a parameter and check the number is prime or no
def prime_number(number):
    half = number / 2
    if number % 2 == 0:
        return False
    for i in range(3, int(half) + 1, 2):
        if number % i == 0:
            print(i)
            return False

    return True

print(prime_number(29))
print(prime_number(8))
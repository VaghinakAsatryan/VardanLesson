#1. Write a program to construct the following pattern.
rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

print("______________________________________________________")

#2. Write a program to create the multiplication table (from 1 to 10) of a number.

num = int(input("Enter the number: "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

print("______________________________________________________")

#3. Write a program to print alphabet pattern 'O'

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)

print("______________________________________________________")


#4. Calculate the sum of all numbers from 1 to a given number from user

num1 = int(input("Enter the number: "))

sum = 0
for i in range(1, num1 + 1):
    sum += i
print(sum)

print("______________________________________________________")

#5. Write a program to check whether a specified list is sorted or not

listA = [11, 9, 0, 7]
print("Given list : ", listA)
listA_copy = listA
listA.sort()

if (listA == listA_copy):
   print("Yes, List is sorted.")
else:
   print("No, List is not sorted.")
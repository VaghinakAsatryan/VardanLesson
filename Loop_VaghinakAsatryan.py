#1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;

num = 1

for i in range(9173, 9435):

   if i % 2 != 0:

       num *= i

print(num)

print("____________________________________________________")
#2*. Print the following pattern

rows = int(input("Enter the number of rows: "))

for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

print("____________________________________________________")

#3. Display numbers from -10 to -1 using for loop

for x in range(-10, 0):
    print(x)

print("____________________________________________________")

#4. Calculate the cube of all numbers from 1 to a given number from user

num1 = int(input("Enter the number: "))

for i in range(1, num1 + 1):
    cub = i ** 3
    print(cub, end='')
    print("\n")

print("____________________________________________________")
#5. Find the factorial of a given number


num2 = int(input("Enter the number: "))

mul = 1
for i in range(1, num2 + 1):
    mul *= i
print("Factorial of", num2, "is", mul)
#1. Write a program to solve (x + y) * (x + y).
     # Test Data : x = 4, y = 3
      #Expected Output : (4 + 3) ^ 2) = 49

x = 4
y = 3
o = 2
z = (x + y) ** o
print("(", x, " + ", y, ") ^", o , "=", z)
print("________________________________________________")

#2. Write a program to parse a string to Float or Integer

age = "25"
height = "165.7"
print("I am ", int(age),  "years old")
print("My height is", float(height),)

print("________________________________________________")

#3. Given variables x=30 and y=20, write a Python program to print "30+20=50" via variables

x = 30
y = 20
z = x + y
print(x, " + ", y, " = ", z)

print("_________________________________________________")

#4. Write a program to get the Type, and Value of an variable


myName = "Vaghinak"
myAge = 21
myHeight = 170.5
IamFromGyumri = True

print(type(myName))
print(type(myAge))
print(type(myHeight))
print(type(IamFromGyumri))

print("____________________________________________________")

#5. Write a program to get the volume of a sphere with radius

r = 2
pi = 3.14
V = 4/3 * pi * r ** 3
print("4/3 * ", pi, " * ", r ** 3, "=", V)

print("____________________________________________________")


#6. Write a program to display your details like name, age, address in three different lines

myName = "Vaghinak"
myLastName = "Asatryan"
myAge = 21
myAdress = "Komitas, Yerevan"

print("Hello " + myName + " " + myLastName)
print("You're ", myAge, " years old")
print("You live in " + myAdress)

print("_______________________________________________________")

#7. Write a program to count the 7% of 500

x = 7
y = 500
percent = x * y / 100
print(x, "% of ", y, "=",  percent)













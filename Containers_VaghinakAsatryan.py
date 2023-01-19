# 1. Write a Python program to get the largest number from a list.

numbers = [0, 12, 25, 26, 28, 654, 234, 201, 129, 165]

numbers.sort()
print(numbers[-1])

print("________________________________________")
# 2. Write a Python program to check a list is empty or not.

if len(numbers) == 0:
    print("List is empty")
else:
    print("List is full")

print("________________________________________")

# 3. Write a Python program to remove all elements from a given set.

club = {"Barcelona", "Real Madrid", "Arsenal"}
club.clear()
print(club)

print("________________________________________")

# 4. Write a Python program to check if a given value is present in a set or not.

club = {"Barcelona", "Real Madrid", "Arsenal"}
searchName = "Atletico"

if searchName in club:
    print("Value is present in a set")
else:
    print("Value isn't present in a set")

print("________________________________________")

# 5. Write a Python program to convert a list to a tuple.

birthdayIsList = [14, 8, 2001, 456, 123, 123, 789, 45]

birthdayIsTuple = tuple(birthdayIsList)

print(birthdayIsTuple)

print("________________________________________")

# 6. Write a Python program to remove an item from a tuple.

birthdayIsList = list(birthdayIsTuple)
birthdayIsList.pop()
birthdayIsTuple = tuple(birthdayIsList)
print(birthdayIsTuple)

print("________________________________________")

# 7. Write a Python script to check whether a given key already exists in a dictionary or not.

myDict = {"Robert Lewandowski": "Barcelona",
          "Lionel Messi": "PSG"}

if "Lionel Messi" in myDict:
    print("Yes, 'Lionel Messi' is one of the keys in the dictionary")
else:
    print("Go out")

print("________________________________________")

# 8. Write a Python script to merge two Python dictionaries.

myDict2 = {"Cristiano Ronaldo": "Manchester United",
           "Karim Benzema": "Real Madrid"}

myDict.update(myDict2)
print(myDict)

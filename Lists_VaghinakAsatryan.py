#01. Write a program to print odd index elements in a list
import statistics

myList = ["Barcelona", "Real Madrid", "Atletico Madrid", "Atletic Bilbao", "Valencia"]


for i in range(1, len(myList), 2):
    print(myList[i])

print("_______________________________________________________________")

#02. Write a program to get the largest number from a list

numbers = [0, 12, 25, 26, 28, 654, 234, 201, 129, 165]

numbers.sort()
print(numbers[-1])

print("_______________________________________________________________")

#03. Write a program to remove duplicates from a list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))

print("_______________________________________________________________")

#04. Write a program to convert a string to a list

song = "The last Christmas I give you my heart"

print(song.split())

print("_______________________________________________________________")

#05. Write a program to find the item with maximum occurrences in a given list

fruit = ["apple", "banana", "banana", "orange", "banana", "apple", "apple", "apple"]



x = statistics.multimode(fruit)
print(x[0])

print("_______________________________________________________________")

#06. Write a program to check whether a specified list is sorted or not

listA = [11,23,65,67,510, 245]
print("Given list : ",listA)
listA.sort()
listA_copy = listA

if (listA == listA_copy):
   print("Yes, List is sorted.")
else:
   print("No, List is not sorted.")

print("_______________________________________________________________")


#07. Write a program to put the words into the correct order

myList = ['Year', 'New', 'Merry', 'and', 'Happy', 'Christmas']

myList[0], myList[2], myList[4] = myList[4], myList[0], myList[2]
print(myList)
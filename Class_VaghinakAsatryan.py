class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.info()

print("______________________________________________________")

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Model: {self.model}\nYear: {self.year}\nColor: {self.color}")

sportCar = Car("Bugatti", 1987 , "Black")

print(sportCar.color)
print("________________")
sportCar.display_info()

print("_____________________________________________________")

class Animal:
    def __init__(self, name, year, weight):
        self.name = name
        self.year = year
        self.weight = weight

    def information(self):
        print(f"Name: {self.name}\nYear: {self.year}\nWeight: {self.weight}")

A1 = Animal("Dog", 8 , 50)

print(A1.name)
print("________________")
A1.information()

print("___________________________________")

class Car:

    color = None
    yaer = None
    name = None

    def __init__(self, color, year, name):

        self.color = color
        self.year = year
        self.name = name

    def info(self):
        print(f"""Color : {self.color}
Name : {self.name}
Year : {self.year}""")

C1 = Car("Black", 18, "07")
C1.info()






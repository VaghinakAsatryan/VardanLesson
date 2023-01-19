print("""1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
 Create a function to display the entire attribute and their values in Student class.
 """)


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"Name: {self.name}\nid: {self.id}")

s1 = Student("Poghos", "0134")

s1.info()

class get_class(Student):
    def __init__(self, className):
        self.className = className

    def info(self):
        print("ClassName:", self.className)

s2 = get_class("First")
s2.info()


print("_________________________________________________________________________")

print("2. Create a Vehicle class without any variables and methods.")

class Vehicle:
    pass

print("__________________________________________________________________________")

print("3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.\n")

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def Vehicle_info(self):
            print(f"Speed: {self.max_speed}\nMileage: {self.mileage}\n")

car = Vehicle(120, 25000)
car.Vehicle_info()

print("_________________________________________________________________")

print("4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class\n")


class Bus(Vehicle):
    pass

school_bus = Bus(180, 12)
print( "Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)

print("___________________________________________________")

print("5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating\n")

class Bus(Vehicle):
    def __init__(self, bus_seating):
        self.bus_seating = bus_seating

    def info(self):
        print("Seating:", self.bus_seating)

school_bus2 = Bus(20)
school_bus2.info()

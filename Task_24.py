# TASK 24

# 1. Create an abstract class called Vehicle
# 2. Create an abstract method called drive_direction()
# 3. Create another class Car that inherits from Vehicle
# 4. Create another class Plane that inherits from Vehicle
# 5. Try running the program and fix the abstract method issues

# Optionally instantiate the Car and Plane method, then invoke the drive_direction() in each of the object instances.

# Hint: the drive_direction() method in your Car should print "Drive forward", ...
#  ...while drive_direction() in your Plane class should print "Drive Upward"


import abc


class Vehicle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drive_direction(self):
        print("Drive")


class Car(Vehicle):
    def drive_direction(self):
        return "Drive forward"


class Plane(Vehicle):
    def drive_direction(self):
        return "Drive upward"


car = Car()
print(car.drive_direction())

plane = Plane()
print(plane.drive_direction())

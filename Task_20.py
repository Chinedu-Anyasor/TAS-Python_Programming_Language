# TASK 20

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add a method called get_gender() that returns "Unknown" in the Human class
# 4. Create another class called Man that extends Human

# Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method
# in each object instance

# Note, to instantiate a class means to create a class.


class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"


class Man(Human):
    def __init__(self):
        self.leg_count = 4


man = Man()

print(man.get_gender())

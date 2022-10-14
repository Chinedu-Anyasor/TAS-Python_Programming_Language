# TASK 19

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add another attribute can_walk with the value of True
# 4. Create a method called get_description, the method should print "This is human"
# 5. Create another method that return the leg count, the name of the method is your choice

class Human:

    def __init__(self):
        self.leg_count = 4
        self.can_walk = "True"

    def get_description(self):
        if self.can_walk == "True":
            print("This is human")
        else:
            print("This is not human")

    def get_leg_numbers(self):
        return self.leg_count


man = Human()
man.get_description()
print(man.get_leg_numbers())

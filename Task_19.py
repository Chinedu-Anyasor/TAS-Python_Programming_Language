# TASK 19

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add another attribute can_walk with the value of True
# 4. Create a method called get_description, the method should print "This is human"
# 5. Create another method that return the leg count, the name of the method is your choice

class Human:

    def __init__(self, leg_count, can_walk):
        self.leg_count = leg_count
        self.can_walk = can_walk

    def get_description(self):
        if self.can_walk == "True":
            print("This is human")
        else:
            print("This is not human")

    def get_leg_numbers(self):
        return self.leg_count


man = Human(4, "True")
print(man.leg_count)
print(man.get_leg_numbers())

man.get_description()

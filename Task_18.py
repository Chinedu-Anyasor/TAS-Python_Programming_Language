# TASK 18

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add another attribute can_walk with value of True

class Human:
    def __init__(self, leg_count, can_walk):
        self.leg_count = leg_count
        self.can_walk = can_walk


man = Human(4, "true")
print(man.can_walk)
print(man.leg_count)

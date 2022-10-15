# TASK 22

# 1. Create a class called Hunt
# 2. Create a private attribute called __weapon with the value "Assault Rifle" in the Hunt class
# 3. Create a method get_weapon() that returns "Not Available" in the Hunt class
# 4. Instantiate an object of the Hunt class
# 5. Print the value of get_weapon() from the object instance

class Hunt:

    __weapon = "Assault Rifle"

    def get_weapon(self):
        return "Not Available"


hunt = Hunt()
print(hunt.get_weapon())

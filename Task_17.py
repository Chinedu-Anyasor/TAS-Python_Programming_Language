# TASK 17

# 1. Create a class called Human
# 2. Initialize the class


class Human:
    def __init__(self, name, sex, height, weight):
        self.name = name
        self.sex = sex
        self.height = height
        self.weight = weight

    def details(self):
        print(
            "My name is " + self.name + ", " + "I am a " + self.sex + ", " + self.height + " tall" + ", " + "My weight is " + self.weight)


student_1 = Human("John", "male", "1.67m", "68kg")
student_1.details()

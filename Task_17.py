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


student_1 = Human("Chinedu", "male", "1.68m", "68kg")
student_2 = Human("Juliet", "female", "1.62m", "72kg")
student_1.details()
student_2.details()

# TASK 8

# 1. Use for loop to iterate from 0 to 10
# 2. For each iteration print out "Number ", i
# 3. If the /i value is equal to 2 add /the /continue
# 4. If the /i value is equal to 8 add the break statement


# Note: For instruction 2, to print out Number and i, use the statement in your loop, print("Number", i)

# 1 and 2.
number = 10
for i in range(number):
    print("Number:", i)

# 3.
number = 10
for i in range(number):
    if i == 2:
        continue
    print("Number", i)

# 4.
number = 10
for i in range(number):
    if i == 8:
        break
    print("Number:", i)

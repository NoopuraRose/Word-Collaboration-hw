# create python program that subtracts two random numbers and prints them and their result  


import random


num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
result = num1 - num2

print("The two random numbers are:", num1, "and", num2)
print("The result of subtracting", num2, "from", num1, "is:", result)
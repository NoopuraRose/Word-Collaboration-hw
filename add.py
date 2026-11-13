#create python program that adds two random numbers and displays them and their result. 
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
result = num1 + num2

print(f"The two random numbers are {num1} and {num2}.")
print(f"Their sum is {result}.")
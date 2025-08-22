
# 1. BUILT-IN FUNCTIONS


# print() -> output dikhata hai
print("Hello Python!")

# input() -> user input (yaha direct value assign kar raha hu)
# name = input("Enter your name: ")  # Console me chalega
name = "Deepak"
print("Name:", name)

# len() -> length
text = "Python"
print("Length:", len(text))

# type() -> data type
print("Type of text:", type(text))

# type conversion (int, float, str)
num = "25"
print("int:", int(num), "float:", float(num), "string:", str(25))

# max(), min(), sum()
numbers = [5, 10, 3, 8]
print("Max:", max(numbers), "Min:", min(numbers), "Sum:", sum(numbers))

# sorted()
print("Sorted list:", sorted(numbers))

# range()
print("Range:", list(range(1, 6)))

# enumerate()
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# map()
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

# filter()
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even:", even)

# open() -> file handling
with open("demo.txt", "w") as f:
    f.write("Hello File!")

with open("demo.txt", "r") as f:
    print("File content:", f.read())

# help()
print("Help on len():")
help(len)


# 2. USER-DEFINED FUNCTION

def greet(name):
    return f"Hello {name}!"

print(greet("Deepak"))

# Function with multiple params
def add(a, b):
    return a + b

print("Add:", add(10, 5))


# 3. LIBRARY FUNCTIONS

# math module
import math
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))

# random module
import random
print("Random number 1-10:", random.randint(1, 10))

# datetime module
import datetime
print("Current DateTime:", datetime.datetime.now())

# os module
import os
print("Current Directory Files:", os.listdir("."))

# Example: OpenCV (cv2) [Image read]
import cv2
img = cv2.imread("demo.jpg")  # agar file ho to read karega
if img is None:
    print("Image not found!")
else:
    print("Image shape:", img.shape)

# Example: PyTorch (torch)
import torch
tensor = torch.tensor([1, 2, 3])
print("Torch Tensor:", tensor)

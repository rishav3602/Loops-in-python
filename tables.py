"""
Write a program to print multiplication table of a given number.
"""

# For loop

num = int(input("Enter the value of number : "))
for i in range (1,11):
    print(f"{num} X {i} = {num*i}")

# While loop

num = int(input("Enter the value of number : "))
i = 1
while i <= 10:
    print(f"{num} X {i} = {num*i}")
    i = i + 1
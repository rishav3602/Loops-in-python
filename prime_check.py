"""
Write a program to check weather a given number is prime or not.
"""

num = int(input("Enter the number you want to check : "))
prime = True
for i in range (2,num):
    if num%i == 0:
        prime = False

if prime :
    print(f"The given number is a prime number")
else:
    print(f"The given number is not a prime number")
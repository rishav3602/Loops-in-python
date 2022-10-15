"""
Write a program to print a multiplication table in reverse order.
"""

n = int(input("Enter your number : "))
for i in range (-10,0,-1):
    print(f"{n} X {-i} = {n*-i}")

"""
Write a program to print factorial of a given number.
"""




n = int(input("Enter the number : "))
fact = 1
for i in range (1,n+1):
    fact = fact * i 
print(f"The factorial of the given number is : {fact}")


n = int(input("Enter the number : "))
fact = 1
i = 0
while i <= n:
    fact = fact * i
    i = i + 1
print(f"The factorial of the given number is : {fact}")
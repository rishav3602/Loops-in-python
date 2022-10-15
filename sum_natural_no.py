"""
Write a program to find the sum of the first n natural numbers.
"""

# For loop

n = int(input("Enter the number till where u need to get the sum : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i 
print(f"The sum of first {n} natural numbers is : {sum}")


# While loop

n = int(input("Enter the number till where u need to get the sum : "))
i = 0 
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print(f"The sum of first {n} natural numbers is : {sum}")

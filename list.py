"""
Write a program to print content of a list using both loops.
"""

# For loop

list = [1,2,3,4,5,6,7,8]
for items in list:
    print(f"The item in the list is : {items}")

# While loop

list = ["Gaurav","Pawan","Sahil","Priyanshu"]
items = 0
while items < len(list):
    print(f" The item in the list is : {list[items]}")
    items = items + 1

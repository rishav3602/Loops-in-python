"""
Write a program to greet all the person stored in the list l1 and whose name startswith "S".
l1 = ["Harry","Sohan","Sachin","Rahul"]
"""

l1 = ["Harry","Sohan","Sachin","Rahul"]
for names in l1:
    if names.startswith("S"):
        print(f"Hello, {names}")
    else:
        pass



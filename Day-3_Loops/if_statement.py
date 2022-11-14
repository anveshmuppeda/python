"""
Program to define if statement
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

i=input("Enter the value of i: ")
j=input("Enter the value of i: ")

#simple if statement
if(i==j):
    print("Both are same")
else:
    print("Both are different")

#nested if statement
if(i>j):
    print("I is greater than J")
elif(i<j):
    print("I is lesser than J")
else:
    print("Both are same")


"""
    Python Program to find the area of triangle
    s = (a+b+c)/2
    area = √(s(s-a)*(s-b)*(s-c))
"""
a = float(input('Enter left side: '))
b = float(input('Enter right side: '))
c = float(input('Enter the third side" '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
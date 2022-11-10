"""
    Python program to swap the two numbers
"""
a = int(input('Enter the value of a: '))
b = int(input('Enteer the value of b: '))
c = a
a = b
b = c
"""
Or we can use the below logic to swap the two numbers
a, b = b, a    
"""
print("Value of a: "+ format(a))
print("Value of b: "+ str(b))
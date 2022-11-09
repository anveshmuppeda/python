# Find square root of real numbers
# Importing the complex math module
import cmath

# To take input from the user
num = eval(input('Enter a number: '))

#find out the square root
num_sqrt = cmath.sqrt(num)

#Printing the results
print('The square root of {0} is {1:0.2f}'.format(num ,num_sqrt.real))

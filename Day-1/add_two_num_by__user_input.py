"""
    Python Program to find the sum of the two numbers from user input
"""
# Store input numbers
number1 = input('Enter first number: ')
number2 = input('Enter second number: ')

# Add two numbers if they are int values we can use int()
int_sum = int(number1) + int(number2)

#Add two numbers if they are float values we can user float()
float_sum = float(number1) + float(number2)

# Display the sum of the two interger values
print('The sum of {0} and {1} is {2}'.format(number1, number2, int_sum))

#Display the sum of the two float values
print('The sum of {0} and {1} is {2}'.format(number1, number2, float_sum))
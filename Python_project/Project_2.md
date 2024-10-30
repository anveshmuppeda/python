# Guess_the_numbers
```python
import random 
number_to_guess = random.randrange(50)
chances = 5
guess_count = 0
while  guess_count < chances:
 guess_count +=1
 my_guess = int(input("Enter your guess number(between 0 to 50): "))
 if my_guess == number_to_guess:
   print("Congratulations you have guess the correct number")
   break
 elif guess_count >= chances and my_guess != number_to_guess:
  print(f"Sorry you have enter a wrong guess and the number is {number_to_guess}")
 elif my_guess > number_to_guess:
  print("your guess number is higher ")
 elif my_guess < number_to_guess:
  print("your guess number is lower ")
  ```
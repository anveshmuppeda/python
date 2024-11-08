# Guess_the_numbers
### Generate a random number and ask the user to guess it. Give hints if the guess is too high or too low.
```python
import random 
guess = random.randrange(50)
chances = 5
guess_count = 0
while  guess_count < chances:
 guess_count +=1
 my_guess = int(input("Enter your guess number(between 0 to 50): "))
 if my_guess == guess:
   print("Congratulations you have guess the correct number")
   break
 elif guess_count >= chances and my_guess != guess:
  print(f"Sorry you have enter a wrong guess and the number is {guess}")
 elif my_guess > guess:
  print("your guess number is higher ")
 elif my_guess < guess:
  print("your guess number is lower ")
  ```
  # Example(output)
Enter your guess number(between 0 to 50): 23
your guess number is lower 
Enter your guess number(between 0 to 50): 24
your guess number is lower 
Enter your guess number(between 0 to 50): 45
your guess number is higher 
Enter your guess number(between 0 to 50): 34
your guess number is lower 
Enter your guess number(between 0 to 50): 39
Sorry you have enter a wrong guess and the number is 38
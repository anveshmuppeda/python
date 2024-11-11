  # Guess_the_numbers
### Generate a random number and ask the user to guess it. Give hints if the guess is too high or too lt  
 This is a game that based on numbers.In this a number is given randomly between the range 0-50.   
 we have to guess the random number.     
 we have five chances of guessing the correct random number.so, if we guess the random number might be  greater than or lower than the random value.if we guess lower number then it shows "your guess number is lower",and if we guess a number that greater than the random number then it shows "your guess number is higher".   
 If our five guesses are incorrect then it shows us as"sorry you have entered a wrong guess",and it shows the random number as the result.
  
  ### Guess_the_numbers Source code
  1. Create a file name [guess_the_numbers.py](./guess_the_numbers.py) with below content
```py
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
  2. Then run the source code with below command.
     ```py
     python guess_the_numbers.py 
  
     ``` 

  
  
  # Example(output)
![Task 2 Output](./../../images/basic-task_2_results.png)
# Integer Errors   
### Create a program that asks the user for an integer input and handles invalid inputs.
```python
try :
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ValueError:
    print("Please enter an integer.")
except ZeroDivisionError:
    print("You cannot divide by zero. ")
except:
    print("Something went wrong")

    print("all done!")
```
# Example(output)
Enter a number: muppeda
Please enter an integer.
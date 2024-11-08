
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    prompt = "Enter an integer: "
    user_input = get_integer_input(prompt)
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()

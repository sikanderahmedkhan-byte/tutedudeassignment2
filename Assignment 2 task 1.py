# Program to check if a number is Even or Odd

def check_even_odd():
    try:
        # Take integer input from the user
        num = int(input("Enter an integer: "))

        # Check if the number is even or odd
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")

    except ValueError:
        # Handle invalid (non-integer) input
        print("Invalid input! Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    check_even_odd()

# tutedudeassignment2

Task 2

# Sum of Integers from 1 to 50

## 📖 Overview
This project demonstrates a simple Python program that calculates the sum of integers from 1 to 50 using a `for` loop.  
It’s a beginner-friendly example to understand iteration, accumulation, and basic function structure in Python.

---

## 🚀 Features
- Uses a `for` loop to iterate through numbers 1 to 50.
- Accumulates the sum in a variable.
- Prints the final result in a clear format.
- Encapsulated in a function for reusability.

---

## 🛠️ Installation
Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/username/sum-integers-1-to-50.git
cd sum-integers-1-to-50

Explanation of code
def sum_integers_1_to_50():
    total_sum = 0  # Initialize sum to zero

    # Iterate from 1 to 50 (inclusive)
    for num in range(1, 51):
        total_sum += num  # Add each number to the sum

    # Display the result
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

if __name__ == "__main__":
    sum_integers_1_to_50()
range(1, 51) generates numbers from 1 to 50.

Each number is added to total_sum.

The final result is printed.

------------------------------------------

Task 1

# Even or Odd Number Checker

## 📖 Overview
This project contains a simple Python program that determines whether a given integer is **Even** or **Odd**.  
It also includes error handling to manage invalid inputs gracefully.

---

## 🚀 Features
- Accepts user input as an integer.
- Checks divisibility by 2 to determine if the number is even or odd.
- Provides clear output messages.
- Handles invalid (non-integer) inputs with an error message.

---

## 🛠️ Installation
Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/username/even-odd-checker.git
cd even-odd-checker

Explanation of code

def check_even_odd():
    try:
        num = int(input("Enter an integer: "))

        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()

num % 2 == 0 → checks if the number is divisible by 2.

If divisible, the number is Even; otherwise, it is Odd.

try-except block ensures invalid inputs are handled properly.

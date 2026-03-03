# tutedudeassignment2

Task 2

# Sum of Integers from 1 to 50
- Uses a `for` loop to iterate through numbers 1 to 50.
- Accumulates the sum in a variable.
- Prints the final result in a clear format.
- Encapsulated in a function for reusability.

Explanation of code
sum_integers_1_to_50():
    total_sum = 0  # Initialize sum to zero

    # from 1 to 50 (inclusive)
    for num in range(1, 51):
        total_sum += num  # Add each number to the sum

    # Display the result
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

range(1, 51) generates numbers from 1 to 50.

Each number is added to total_sum.

The final result is printed.

------------------------------------------

Task 1

# Even or Odd Number Checker

- Accepts user input as an integer.
- Checks divisibility by 2 to determine if the number is even or odd.
- Provides clear output messages.

Explanation of code

check_even_odd():
        num = int(input("Enter an integer: "))

        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")


num % 2 == 0 → checks if the number is divisible by 2.

If divisible, the number is Even; otherwise, it is Odd.


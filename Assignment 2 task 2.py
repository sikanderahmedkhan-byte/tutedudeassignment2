# Task 2: Sum of Integers from 1 to 50 Using a Loop

def sum_integers_1_to_50():
    total_sum = 0  # Initialize sum to zero

    # Iterate from 1 to 50 (inclusive)
    for num in range(1, 51):
        total_sum += num  # Add each number to the sum

    # Display the result
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

# Run the function
if __name__ == "__main__":
    sum_integers_1_to_50()

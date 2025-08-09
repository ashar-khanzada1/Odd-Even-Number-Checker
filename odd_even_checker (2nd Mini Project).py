# Odd and Even Number Checker
# Author: Ashar Khanzada
# Date: 2025-08-10
# Description: A mini-project to check if a number is odd or even.

print("Welcome to the Odd & Even Checker")

while True:
    # Take input from the user
    digit = int(input("Enter a number: "))

    # Check if the number is even or odd
    if digit % 2 == 0:
        print(f"{digit} is Even")
    else:
        print(f"{digit} is Odd")

    # Ask user if they want to check again
    digit_1 = input("Want to check again? (Han/Na): ").strip().lower()
    if digit_1 == "na":
        print("Thanks for using the program!")
        break

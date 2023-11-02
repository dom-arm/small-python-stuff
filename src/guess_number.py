import random

# Command line game:
# 1. The computer will think of 3 digit number that has no repeating digits
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
# Match: You've guessed a correct digit in the correct position
# Close: You've guessed a correct digit but in the wrong position
# Nope: You haven't guess any of the digits correctly
# 4. Based on these clues you will guess again until you break the code with a perfect match!


def generate_3_digit_num():
    # Generate list of unordered digits from 0-9
    digits = list(range(10))
    random.shuffle(digits)

    # Convert each digit in the list to strings
    str_digits = [str(digit) for digit in digits]

    # Slice the list to contain 3 digits
    str_digits = str_digits[:3]

    # Join list of digits to be a string and return it
    return "".join(str_digits)


def matches(num1, num2):
    isMatch = False
    if num1 == num2:
        isMatch = True
        print("Perfect match!")
    elif num1[0] == num2[0] or num1[1] == num2[1] or num1[2] == num2[2]:
        print("Match: You've guessed a correct digit in the correct position")
    elif num1[0] in num2 or num1[1] in num2 or num1[2] in num2:
        print("Close: You've guessed a correct digit but in the wrong position")
    else:
        print("Nope: You haven't guess any of the digits correctly")
    return isMatch


def main():
    computers_num = generate_3_digit_num()
    # print(computers_num)  # For testing
    users_guess = input("What is your guess?\n")

    # The comparison should return True when it's a match, and we can stop ask for new guess
    while not matches(computers_num, users_guess):
        users_guess = input("What is your guess?\n")


main()

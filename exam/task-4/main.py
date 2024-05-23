# Function: FizzBuzz
# Objective: Create a function `fizz_buzz` that evaluates the divisibility of a number by 3 and 5.
# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the number as a string.
# Parameters:
# - num: An integer to be evaluated.
# Returns:
# - A string based on the criteria above.

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

print(fizz_buzz(7))
print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(15))

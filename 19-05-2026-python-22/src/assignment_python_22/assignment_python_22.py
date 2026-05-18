"""Python 22 assignment: understanding and using conditional statements.

PART 1: Understanding Conditional Statements

1. Role of conditional statements:
   a) if statement:
      Executes a block of code only if a condition is True.
      Syntax: if condition:
      Example: if age < 13: print("You are a child")

   b) elif statement (else if):
      Allows checking multiple conditions in sequence.
      Executes only if previous if/elif conditions were False.
      Syntax: elif condition:
      Example: elif age < 20: print("You are a teenager")

   c) else statement:
      Executes a block of code if all previous if/elif conditions were False.
      Catches all remaining cases without an explicit condition.
      Syntax: else:
      Example: else: print("You are an adult")

2. Output of the given code:
   x = 10
   y = 20
   if x > y:
       print("x is greater than y")
   elif x < y:
       print("x is less than y")
   else:
       print("x and y are equal")

   EXPECTED OUTPUT: "x is less than y"
   (Because 10 > 20 is False, so we check 10 < 20 which is True)
"""

from __future__ import annotations


def classify_age(age: int) -> str:
    """Classifies age into child, teenager, or adult.

    Args:
        age: The person's age in years.

    Returns:
        A string describing the age category.
    """

    if age < 13:
        return "You are a child"
    elif age < 20:
        return "You are a teenager"
    else:
        return "You are an adult"


def compare_numbers(num1: float, num2: float) -> str:
    """Compares two numbers and returns which is larger.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        String indicating which number is larger or if they're equal.
    """

    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num1 < num2:
        return f"{num2} is larger than {num1}"
    else:
        return f"{num1} and {num2} are equal"


def check_even_odd(num: int) -> str:
    """Checks if a number is even or odd.

    Args:
        num: The number to check.

    Returns:
        String indicating whether the number is even or odd.
    """

    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


def check_sign(num: float) -> str:
    """Checks whether a number is positive, negative, or zero.

    Args:
        num: The number to check.

    Returns:
        String indicating the sign of the number.
    """

    if num > 0:
        return f"{num} is positive"
    elif num < 0:
        return f"{num} is negative"
    else:
        return f"{num} is zero"


def main() -> None:
    """Runs all conditional statement examples."""

    print("=== PART 2: Writing Your Own Conditional Statements ===\n")

    # Task 3: Age classification
    print("Task 3: Age Classification")
    age_input = input("Enter your age: ")
    age = int(age_input)
    print(classify_age(age))
    print()

    # Task 4: Compare two numbers
    print("Task 4: Compare Two Numbers")
    num1_input = input("Enter first number: ")
    num2_input = input("Enter second number: ")
    num1 = float(num1_input)
    num2 = float(num2_input)
    print(compare_numbers(num1, num2))
    print()

    # Task 5: Even or odd
    print("Task 5: Even or Odd")
    even_odd_input = input("Enter a number: ")
    even_odd_num = int(even_odd_input)
    print(check_even_odd(even_odd_num))
    print()

    # Task 6: Check sign of number
    print("Task 6: Check Sign (Positive, Negative, Zero)")
    sign_input = input("Enter a number: ")
    sign_num = float(sign_input)
    print(check_sign(sign_num))


if __name__ == "__main__":
    main()

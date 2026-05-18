"""Python 23 assignment: counting numbers with while loops."""

from __future__ import annotations


def count_to_ten() -> None:
    """Prints numbers from 1 to 10 using a while loop."""

    print("Task 1: Numbers 1 to 10")
    print("-" * 30)

    i = 1
    while i <= 10:
        print(i)
        i += 1

    print()


def count_tens() -> None:
    """Prints every tenth number from 10 to 100 using a while loop."""

    print("Task 2: Every tenth number (10 to 100)")
    print("-" * 30)

    i = 10
    while i <= 100:
        print(i)
        i += 10

    print()


def count_divisible_by_three() -> None:
    """Prints all numbers divisible by 3 from 1 to 1000 using a while loop.

    Also counts and displays the total count of such numbers.
    """

    print("Task 3: Numbers divisible by 3 (1 to 1000)")
    print("-" * 30)

    i = 1
    count = 0

    while i <= 1000:
        if i % 3 == 0:
            print(i)
            count += 1
        i += 1

    print()
    print(f"Total numbers divisible by 3 in range 1-1000: {count}")
    print()


def main() -> None:
    """Runs all three while loop tasks."""

    count_to_ten()
    count_tens()
    count_divisible_by_three()


if __name__ == "__main__":
    main()

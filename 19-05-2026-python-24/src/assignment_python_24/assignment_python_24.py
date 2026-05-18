"""Python 24 assignment: for loop operations on lists, strings, and ranges."""

from __future__ import annotations


def task_1_print_fruits() -> None:
    """Task 1: Create a list of 4 fruits and print each on a separate line."""

    fruits = ["apple", "banana", "orange", "grape"]

    print("Task 1: Fruits")
    for fruit in fruits:
        print(fruit)
    print()


def task_2_print_word_chars() -> None:
    """Task 2: Ask for a word and print each character on a separate line."""

    word = input("Enter a word: ").strip()

    print("Task 2: Characters in word")
    for char in word:
        print(char)
    print()


def task_3_print_range() -> None:
    """Task 3: Use range() to print numbers from 1 to 5."""

    print("Task 3: Numbers 1 to 5")
    for number in range(1, 6):
        print(number)
    print()


def task_4_count_vowels() -> None:
    """Task 4: Count vowels in a user-entered sentence."""

    sentence = input("Enter a sentence: ").strip()

    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    print("Task 4: Vowel Counter")
    print(f"Sentence: {sentence}")
    print(f"Total vowels found: {vowel_count}")
    print()


def main() -> None:
    """Runs all four tasks."""

    print("Python 24 - For Loops Assignment\n")

    task_1_print_fruits()
    task_2_print_word_chars()
    task_3_print_range()
    task_4_count_vowels()

    print("All tasks completed.")


if __name__ == "__main__":
    main()

"""Assignment 3 solution: lists and loops."""

from __future__ import annotations


def create_fruits() -> list[str]:
    """Creates the initial list of fruits.

    Returns:
        A list with five fruit names.
    """

    return ["apple", "banana", "orange", "kiwi", "mango"]


def print_second_and_last(fruits: list[str]) -> None:
    """Prints the second and last fruit from the list.

    Args:
        fruits: Source list of fruits.

    Raises:
        ValueError: If there are fewer than two fruits in the list.
    """

    if len(fruits) < 2:
        raise ValueError("At least two fruits are required.")

    print(f"Second fruit: {fruits[1]}")
    print(f"Last fruit: {fruits[-1]}")


def add_and_remove_fruit(fruits: list[str], fruit_to_add: str) -> list[str]:
    """Adds one fruit and removes the first fruit.

    Args:
        fruits: Source list of fruits.
        fruit_to_add: Fruit to append at the end.

    Returns:
        Updated list after append and first-item removal.
    """

    updated_fruits = fruits.copy()
    updated_fruits.append(fruit_to_add)
    del updated_fruits[0]
    return updated_fruits


def print_fruits_with_for_loop(fruits: list[str]) -> None:
    """Prints each fruit using a for loop.

    Args:
        fruits: List of fruits to print.
    """

    print("Fruits in the list:")
    for fruit in fruits:
        print(f"- {fruit}")


def print_numbers_with_while_loop(start: int = 1, end: int = 10) -> None:
    """Prints numbers from start to end using a while loop.

    Args:
        start: First number to print.
        end: Last number to print.
    """

    print("Numbers from 1 to 10:")
    current = start
    while current <= end:
        print(current)
        current += 1


def main() -> None:
    """Runs all tasks from Assignment 3."""

    fruits = create_fruits()
    print_second_and_last(fruits)

    fruits = add_and_remove_fruit(fruits, "grape")
    print_fruits_with_for_loop(fruits)

    print_numbers_with_while_loop()


if __name__ == "__main__":
    main()

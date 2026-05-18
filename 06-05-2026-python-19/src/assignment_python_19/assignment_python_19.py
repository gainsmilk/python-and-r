"""Python 19 assignment: tuple operations and immutability."""

from __future__ import annotations


def demonstrate_tuple_creation() -> tuple:
    """Creates and returns a tuple with mixed data types.

    Returns:
        A tuple containing at least 5 elements.
    """

    my_tuple = ("Python", 19, 3.14, True, "immutable")
    return my_tuple


def demonstrate_immutability() -> None:
    """Attempts to modify a tuple and catches the resulting error.

    Shows that tuples are immutable by trying to change an element,
    which raises a TypeError.
    """

    my_tuple = (10, 20, 30, 40, 50)

    try:
        my_tuple[0] = 999
    except TypeError as e:
        print(f"Error caught: {e}")


def demonstrate_indexing_and_slicing() -> None:
    """Shows tuple indexing and slicing operations.

    Demonstrates accessing single elements and ranges.
    """

    numbers = (2, 4, 6, 8, 10, 12, 14)

    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Middle three elements: {numbers[2:5]}")
    print(f"Every other element: {numbers[::2]}")


def demonstrate_tuple_methods() -> None:
    """Demonstrates the .count() and .index() methods on tuples.

    .count() returns how many times an element appears.
    .index() returns the position of the first occurrence.
    """

    grades = (85, 92, 78, 92, 88, 92, 95)

    count_92 = grades.count(92)
    print(f"Grade 92 appears {count_92} times")

    first_position_92 = grades.index(92)
    print(f"First 92 is at index {first_position_92}")


def demonstrate_tuple_unpacking() -> None:
    """Unpacks a tuple into multiple variables.

    Shows how to assign tuple elements directly to separate variables.
    """

    person = ("Alice", 25, "Warsaw", "alice@example.com")

    name, age, city, email = person
    print(f"{name} is {age} years old, lives in {city}, email: {email}")


def demonstrate_tuple_as_dict_key() -> None:
    """Shows using a tuple as a dictionary key.

    Since tuples are immutable and hashable, they can be used as dict keys,
    whereas lists cannot.
    """

    coordinates = {}

    location_a = (10, 20)
    location_b = (15, 25)
    location_c = (10, 20)

    coordinates[location_a] = "Building A"
    coordinates[location_b] = "Building B"
    coordinates[location_c] = "Same as Building A (overwrites)"

    print("Dictionary with tuple keys:")
    for coord, place in coordinates.items():
        print(f"  {coord} -> {place}")


def main() -> None:
    """Runs all tuple demonstrations."""

    print("=== Tuple Creation ===")
    my_tuple = demonstrate_tuple_creation()
    print(f"Created tuple: {my_tuple}\n")

    print("=== Immutability ===")
    demonstrate_immutability()
    print()

    print("=== Indexing and Slicing ===")
    demonstrate_indexing_and_slicing()
    print()

    print("=== Tuple Methods ===")
    demonstrate_tuple_methods()
    print()

    print("=== Tuple Unpacking ===")
    demonstrate_tuple_unpacking()
    print()

    print("=== Tuples as Dictionary Keys ===")
    demonstrate_tuple_as_dict_key()


if __name__ == "__main__":
    main()

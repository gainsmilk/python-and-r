"""Python 21 assignment: student profile manager using dictionaries."""

from __future__ import annotations


def create_student_profile() -> dict[str, str | int | float]:
    """Creates and returns a student profile dictionary.

    Returns:
        A dictionary with student details.
    """

    student = {
        "name": "Alice Johnson",
        "student_id": 12345,
        "major": "Computer Science",
        "gpa": 3.85,
        "semester": 4,
        "email": "alice@university.edu"
    }
    return student


def display_profile(student: dict[str, str | int | float]) -> None:
    """Prints the student profile in a formatted way.

    Args:
        student: A dictionary containing student information.
    """

    print("--- Student Profile ---")
    for key, value in student.items():
        print(f"{key.title()}: {value}")


def main() -> None:
    """Demonstrates dictionary operations using a student profile."""

    # Task 1: Create a dictionary with at least 5 key-value pairs
    student = create_student_profile()
    print("Task 1: Created student profile")
    display_profile(student)
    print()

    # Task 2: Access a value by its key
    print("Task 2: Access a value by key")
    name = student["name"]
    print(f"Student name: {name}")
    print()

    # Task 3: Add a new key-value pair
    print("Task 3: Add a new key-value pair")
    student["phone"] = "555-0123"
    print(f"Added phone: {student['phone']}")
    print()

    # Task 4: Update an existing value
    print("Task 4: Update an existing value")
    print(f"Previous GPA: {student['gpa']}")
    student["gpa"] = 3.92
    print(f"Updated GPA: {student['gpa']}")
    print()

    # Task 5: Delete a key-value pair
    print("Task 5: Delete a key-value pair")
    if "phone" in student:
        del student["phone"]
        print("Removed phone key")
    print()

    # Task 6: Demonstrate .get(), .keys(), .values(), and .items()
    print("Task 6: Dictionary methods")

    # .get() - safe access with default value
    print("Using .get() with default value:")
    office = student.get("office", "Not assigned")
    print(f"Office: {office}")
    print()

    # .keys() - get all keys
    print("Using .keys():")
    print(f"Keys: {list(student.keys())}")
    print()

    # .values() - get all values
    print("Using .values():")
    print(f"Values: {list(student.values())}")
    print()

    # .items() - get key-value pairs
    print("Using .items():")
    for key, value in student.items():
        print(f"  {key} -> {value}")
    print()

    # Task 7: Iterate over the dictionary using a for loop
    print("Task 7: Iterate using a for loop")
    print("Iterating over keys:")
    for key in student:
        print(f"  {key}: {student[key]}")


if __name__ == "__main__":
    main()

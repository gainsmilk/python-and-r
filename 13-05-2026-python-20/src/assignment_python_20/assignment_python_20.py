"""Python 20 assignment: sets operations and methods."""

from __future__ import annotations


def main() -> None:
    """Demonstrates set creation, operations, and methods."""

    # Task 1: Create a set with at least six unique elements.
    print("=" * 60)
    print("Task 1: Create a set with unique elements")
    print("=" * 60)

    fruits = {"apple", "banana", "orange", "grape", "mango", "kiwi"}
    print(f"Original set: {fruits}")
    print(f"Set type: {type(fruits)}")
    print(f"Set length: {len(fruits)}")
    print()

    # Task 2: Access a set item using iteration.
    # (Sets do not support indexing like lists do)
    print("=" * 60)
    print("Task 2: Access set items via iteration")
    print("=" * 60)
    print("Iterating through the set:")

    for fruit in fruits:
        print(f"  - {fruit}")

    print()

    # Task 3: Add a new item to the set.
    print("=" * 60)
    print("Task 3: Add a new item using .add()")
    print("=" * 60)

    print(f"Before: {fruits}")
    fruits.add("pineapple")
    print(f"After .add('pineapple'): {fruits}")
    print()

    # Task 4: Remove an existing item from the set.
    print("=" * 60)
    print("Task 4: Remove an item using .remove()")
    print("=" * 60)

    print(f"Before: {fruits}")
    fruits.remove("banana")
    print(f"After .remove('banana'): {fruits}")
    print()

    # Task 5: Perform a union operation on two sets.
    print("=" * 60)
    print("Task 5: Union operation (.union() or |)")
    print("=" * 60)

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")

    union_result = set_a.union(set_b)
    print(f"Union (A | B): {union_result}")
    print("(Note: Union contains all unique elements from both sets)")
    print()

    # Task 6: Perform an intersection operation on two sets.
    print("=" * 60)
    print("Task 6: Intersection operation (.intersection() or &)")
    print("=" * 60)

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")

    intersection_result = set_a.intersection(set_b)
    print(f"Intersection (A & B): {intersection_result}")
    print("(Note: Intersection contains only elements present in both sets)")
    print()

    # Task 7: Use at least two set methods and explain their usage.
    print("=" * 60)
    print("Task 7: Additional set methods")
    print("=" * 60)

    numbers = {10, 20, 30, 40, 50}
    print(f"Original set: {numbers}")

    # Method 1: .pop() - removes and returns an arbitrary element
    print("\nMethod 1: .pop()")
    popped_value = numbers.pop()
    print(f"  Removed value: {popped_value}")
    print(f"  Set after .pop(): {numbers}")
    print("  (Note: .pop() removes an arbitrary element since sets are unordered)")

    # Method 2: .clear() - removes all elements from the set
    print("\nMethod 2: .clear()")
    test_set = {7, 8, 9}
    print(f"  Before .clear(): {test_set}")
    test_set.clear()
    print(f"  After .clear(): {test_set}")
    print("  (Note: The set is now empty but still exists)")

    # Method 3: .difference() - returns elements in set A but not in set B
    print("\nMethod 3: .difference() (bonus)")
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7}
    difference = set_x.difference(set_y)
    print(f"  Set X: {set_x}")
    print(f"  Set Y: {set_y}")
    print(f"  Difference (X - Y): {difference}")
    print("  (Note: Contains elements in X that are not in Y)")

    print()
    print("=" * 60)
    print("All tasks completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

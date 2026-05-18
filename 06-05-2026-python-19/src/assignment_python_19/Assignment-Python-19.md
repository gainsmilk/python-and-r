# Python 19 - Tuples

Explores tuple operations, immutability, unpacking, and using tuples as dictionary keys. User sees practical examples of why tuples are faster than lists and hashable (unlike lists). Script creates a sample tuple, attempts to modify it with error handling, demonstrates indexing/slicing, uses `.count()` and `.index()` methods, unpacks a tuple into variables, and shows how tuples can be dictionary keys.

## Functionalities used

- Tuple creation (1): `my_tuple = ("Python", 19, 3.14, True, "immutable")`
- Indexing (3): first element, last element via negative index, single element access
- Slicing (3): range slice, negative indices, step slicing
- Immutability with try/except (1): attempt modification and catch TypeError
- Tuple methods (2): `.count()`, `.index()`
- Tuple unpacking (1): `name, age, city, email = person`
- Dictionary with tuple keys (1): using tuples as hashable keys
- For loops (1): iterate over dictionary items
- Type hints (8): function annotations with tuple return types

## Run

```bash
python assignment_python_19.py
```

## Expected output

```
=== Tuple Creation ===
Created tuple: ('Python', 19, 3.14, True, 'immutable')

=== Immutability ===
Error caught: 'tuple' object does not support item assignment

=== Indexing and Slicing ===
First element: 2
Last element: 14
Middle three elements: (6, 8, 10)
Every other element: (2, 6, 10, 14)

=== Tuple Methods ===
Grade 92 appears 3 times
First 92 is at index 1

=== Tuple Unpacking ===
Alice is 25 years old, lives in Warsaw, email: alice@example.com

=== Tuples as Dictionary Keys ===
Dictionary with tuple keys:
  (10, 20) -> Same as Building A (overwrites)
  (15, 25) -> Building B
```

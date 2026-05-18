# Python 20 - Sets

Demonstrates set creation, iteration, modification via `.add()` and `.remove()`, and mathematical operations (union, intersection, difference). Also covers additional set methods like `.pop()` and `.clear()` to show the full capabilities of the set data structure.

## Functionalities used

- Set creation (1): `fruits = {"apple", "banana", ...}`
- Set iteration (1): `for fruit in fruits:`
- Set methods (6): `.add()`, `.remove()`, `.union()`, `.intersection()`, `.pop()`, `.clear()`, `.difference()`
- Operators (3): `|` (union), `&` (intersection), `-` (difference)
- Type checking (1): `type(fruits)`
- Built-in functions (2): `len()`, `print()`
- Conditional logic (1): implicit via method usage
- String formatting (3): f-strings for output

## Run

```bash
python assignment_python_20.py
```

## Expected output

```
============================================================
Task 1: Create a set with unique elements
============================================================
Original set: {'apple', 'banana', 'orange', 'grape', 'mango', 'kiwi'}
Set type: <class 'set'>
Set length: 6

============================================================
Task 2: Access set items via iteration
============================================================
Iterating through the set:
  - apple
  - banana
  - orange
  - grape
  - mango
  - kiwi

============================================================
Task 3: Add a new item using .add()
============================================================
Before: {'apple', 'banana', 'orange', 'grape', 'mango', 'kiwi'}
After .add('pineapple'): {'apple', 'banana', 'orange', 'grape', 'mango', 'kiwi', 'pineapple'}

============================================================
Task 4: Remove an item using .remove()
============================================================
Before: {'apple', 'banana', 'orange', 'grape', 'mango', 'kiwi', 'pineapple'}
After .remove('banana'): {'apple', 'orange', 'grape', 'mango', 'kiwi', 'pineapple'}

============================================================
Task 5: Union operation (.union() or |)
============================================================
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
Union (A | B): {1, 2, 3, 4, 5, 6}
(Note: Union contains all unique elements from both sets)

============================================================
Task 6: Intersection operation (.intersection() or &)
============================================================
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
Intersection (A & B): {3, 4}
(Note: Intersection contains only elements present in both sets)

============================================================
Task 7: Additional set methods
============================================================
Original set: {10, 20, 30, 40, 50}

Method 1: .pop()
  Removed value: 10
  Set after .pop(): {20, 30, 40, 50}
  (Note: .pop() removes an arbitrary element since sets are unordered)

Method 2: .clear()
  Before .clear(): {7, 8, 9}
  After .clear(): set()
  (Note: The set is now empty but still exists)

Method 3: .difference() (bonus)
  Set X: {1, 2, 3, 4, 5}
  Set Y: {4, 5, 6, 7}
  Difference (X - Y): {1, 2, 3}
  (Note: Contains elements in X that are not in Y)

============================================================
All tasks completed!
============================================================
```

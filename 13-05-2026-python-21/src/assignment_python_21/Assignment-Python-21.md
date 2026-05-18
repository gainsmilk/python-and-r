# Python 21 - Dictionaries

Student profile manager that demonstrates core dictionary operations. User creates a student profile dictionary, accesses values, adds/updates/deletes keys, and explores dictionary methods (.get(), .keys(), .values(), .items()).

## Functionalities used

- Dictionary creation (1): `create_student_profile()` returns a dict with 6 key-value pairs
- Dictionary access (1): `student["name"]` direct key access
- Dictionary addition (1): `student["phone"] = "555-0123"`
- Dictionary update (1): `student["gpa"] = 3.92`
- Dictionary deletion (1): `del student["phone"]`
- Conditional check (1): `if "phone" in student`
- Dictionary methods (4): `.get()`, `.keys()`, `.values()`, `.items()`
- For loops (3): iterate over keys, iterate over items, iterate over values
- Type hints (2): `dict[str, str | int | float]` for function args and returns
- Formatted output (2): `.title()` for key formatting, f-strings for display

## Run

```bash
python assignment_python_21.py
```

## Expected output

```
Task 1: Created student profile
--- Student Profile ---
Name: Alice Johnson
Student_id: 12345
Major: Computer Science
Gpa: 3.85
Semester: 4
Email: alice@university.edu

Task 2: Access a value by key
Student name: Alice Johnson

Task 3: Add a new key-value pair
Added phone: 555-0123

Task 4: Update an existing value
Previous GPA: 3.85
Updated GPA: 3.92

Task 5: Delete a key-value pair
Removed phone key

Task 6: Dictionary methods
Using .get() with default value:
Office: Not assigned

Using .keys():
Keys: ['name', 'student_id', 'major', 'gpa', 'semester', 'email']

Using .values():
Values: ['Alice Johnson', 12345, 'Computer Science', 3.92, 4, 'alice@university.edu']

Using .items():
  name -> Alice Johnson
  student_id -> 12345
  major -> Computer Science
  gpa -> 3.92
  semester -> 4
  email -> alice@university.edu

Task 7: Iterate using a for loop
Iterating over keys:
  name: Alice Johnson
  student_id: 12345
  major: Computer Science
  gpa: 3.92
  semester: 4
  email: alice@university.edu
```

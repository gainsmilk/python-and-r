# Python 22 - Conditional Statements

Introduction to `if`, `elif`, and `else` statements. User-driven programs that classify ages, compare numbers, check parity, and determine sign.

## Part 1: Understanding Conditional Statements

### 1. Role of Each Statement

**a) if statement**

The `if` statement executes a block of code only if a condition evaluates to `True`. It is the foundation of all conditional logic in Python.

```python
if condition:
    # code runs only if condition is True
```

Example: `if age < 13: print("You are a child")`

**b) elif statement (else if)**

The `elif` statement allows you to check multiple conditions in sequence. It only executes if the previous `if` or `elif` condition was `False`. You can chain multiple `elif` statements together.

```python
elif condition:
    # code runs only if previous conditions were False and this is True
```

Example: `elif age < 20: print("You are a teenager")`

**c) else statement**

The `else` statement provides a fallback block of code that runs if all previous `if` and `elif` conditions were `False`. It requires no condition and catches all remaining cases.

```python
else:
    # code runs if all previous conditions were False
```

Example: `else: print("You are an adult")`

### 2. Output Prediction

Given code:
```python
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")
```

**Expected Output:**
```
x is less than y
```

**Explanation:** The condition `x > y` (10 > 20) is `False`, so we skip the `if` block. The condition `x < y` (10 < 20) is `True`, so we execute the `elif` block and print "x is less than y". The `else` block never runs.

## Part 2: Writing Your Own Conditional Statements

### 3. Age Classification Program

**Functionality:** Asks user for age and classifies into three categories.

**Sample Input / Output:**
```
Enter your age: 15
You are a teenager
```

**Another example:**
```
Enter your age: 8
You are a child
```

**Another example:**
```
Enter your age: 25
You are an adult
```

### 4. Compare Two Numbers Program

**Functionality:** Takes two numbers and prints which is larger, or if equal.

**Sample Input / Output:**
```
Enter first number: 45
Enter second number: 32
32 is larger than 45
```

Wait, let me correct that. The larger number is 45, so:
```
Enter first number: 45
Enter second number: 32
45 is larger than 32
```

**Another example:**
```
Enter first number: 100
Enter second number: 100
100 and 100 are equal
```

### 5. Even or Odd Program

**Functionality:** Asks for a number and checks if it is even or odd using the modulo operator `%`.

**Sample Input / Output:**
```
Enter a number: 7
7 is odd
```

**Another example:**
```
Enter a number: 42
42 is even
```

**Note:** A number is even if `num % 2 == 0` (remainder is 0), odd otherwise.

### 6. Check Sign of Number

**Functionality:** Determines whether a given number is positive, negative, or zero.

**Sample Input / Output:**
```
Enter a number: -15
-15 is negative
```

**Another example:**
```
Enter a number: 0
0 is zero
```

**Another example:**
```
Enter a number: 3.5
3.5 is positive
```

## Functionalities Used

- Conditional statements (if/elif/else): 4 tasks + 1 in Part 1 = 5 separate conditional blocks
- Multiple inputs (5): age, num1, num2, even_odd_num, sign_num
- Type conversion (4): `int()`, `float()` for user input
- Comparison operators (6): `<`, `>`, `==`, `!=` across multiple programs
- Arithmetic operators (1): modulo `%` for even/odd check
- Return statements (4): functions return strings
- String formatting (1): f-strings in comparison output

## Run

```bash
python assignment_python_22.py
```

The program runs interactively, asking for input for each of the 4 tasks in sequence.

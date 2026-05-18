# Python 23 - Counting Numbers with a While Loop

While loops repeat a block of code as long as a condition is true. Unlike for loops which iterate a known number of times, while loops are useful when we don't know the exact number of repetitions in advance. This assignment practices basic while loop structure with counter variables.

## Approach

- Use a counter variable (e.g. `i`) to track loop progress
- Increment the counter inside the loop body to avoid infinite loops
- Use comparison operators (`<=`, `<`) in the while condition
- Apply modulo (`%`) for divisibility checks when needed

## Tasks

### Task 1: Numbers 1 to 10
Print all numbers from 1 to 10, one per line, using a while loop.

**Implementation:** Counter starts at 1, increments by 1 each iteration, stops when counter exceeds 10.

**Sample output:**
```
1
2
3
...
10
```

### Task 2: Every Tenth Number (10 to 100)
Print every tenth value in the range 1 to 100 (10, 20, 30, ..., 100).

**Implementation:** Counter starts at 10, increments by 10 each iteration, stops when counter exceeds 100.

**Sample output:**
```
10
20
30
...
100
```

### Task 3: Numbers Divisible by 3 (1 to 1000) with Count
Print all numbers from 1 to 1000 that are divisible by 3. Also display the total count of such numbers.

**Implementation:** Counter starts at 1, increments by 1. Use modulo operator (`i % 3 == 0`) to check divisibility. Maintain a separate count variable, incremented whenever a number passes the divisibility check.

**Sample output:**
```
3
6
9
...
999

Total numbers divisible by 3 in range 1-1000: 333
```

## Functionalities used

- While loops (3): counter-based repetition with condition checking
- Counter variables (4): i, i, i+count
- Increment operators (3): `i += 1`, `i += 10`, `i += 1`
- Conditional statements (1): divisibility check `i % 3 == 0`
- Modulo operator (1): remainder check for divisibility
- Print statements (9): task headers, dividers, output, summary

## Run

```bash
python assignment_python_23.py
```

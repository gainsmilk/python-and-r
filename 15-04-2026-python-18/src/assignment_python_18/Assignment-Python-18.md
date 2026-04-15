# Python 18 - 1RM Calculator

Simple bench press 1-rep-max estimator. User enters their name, exercise, weight lifted, and reps. Script computes 1RM via Epley and Brzycki formulas, prints a greeting built via string slicing + concatenation, and classifies the result.

## Functionalities used

- Multiple inputs (4): name, exercise, weight, reps
- Mathematical calculations (4): Epley formula, Brzycki formula, average, round
- String slicing (1): `name[:3]`
- String methods (3): `.strip()`, `.upper()`, `.title()`
- Concatenations (1): `"hi " + name[:3].upper() + ", lets see your numbers."`
- Conditional statements (5): rep sanity check, 4 branches in `rating()` (beginner / intermediate / advanced / elite), `epley vs brzycki` selector
- For loops (1): iterate over `formulas`
- List methods (2): `.append()`, `.sort()`

## Run

```bash
python assignment_python_18.py
```

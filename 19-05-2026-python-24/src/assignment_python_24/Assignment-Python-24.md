# Python 24 - For Loops

For loop practice. Tasks cover iterating through lists, strings, and ranges, plus conditional logic inside a loop.

## Functionalities used

- For loops (4): iterate over list, string, range, and string with condition
- Lists (1): fruit list with 4 items
- input() (2): word entry, sentence entry
- String iteration (2): character-by-character in word and sentence
- range() (1): numbers 1 to 5
- Conditional checks (1): vowel detection with `in` operator
- Counter logic (1): vowel accumulation
- String slicing / membership (1): vowel string for lookup

## Tasks

**Task 1:** Create a list of 4 fruits. Use a for loop to print each fruit on a separate line.

**Task 2:** Ask the user to enter a word. Use a for loop to print each character of the word on a separate line.

**Task 3:** Use a for loop with the range() function to print numbers from 1 to 5. Each number should be printed on a separate line.

**Task 4:** Ask the user to enter a sentence. Use a for loop to go through each character in the sentence. Count how many vowels (a, e, i, o, u) appear in the sentence (both lowercase and uppercase). At the end, print the total number of vowels found.

## Approach

- Each task is its own function for clarity and modularity.
- Task 1 uses a hardcoded list; Tasks 2 and 4 use `input()` for interactivity.
- Task 3 demonstrates `range(1, 6)` to generate 1 through 5.
- Task 4 handles case-insensitivity by checking both uppercase and lowercase vowels in a single string lookup.
- Vowel counter increments for each matching character.

## Sample Output

```
Python 24 - For Loops Assignment

Task 1: Fruits
apple
banana
orange
grape

Task 2: Characters in word
Enter a word: hello
h
e
l
l
o

Task 3: Numbers 1 to 5
1
2
3
4
5

Task 4: Vowel Counter
Enter a sentence: Hello, how are you?
Sentence: Hello, how are you?
Total vowels found: 8

All tasks completed.
```

## Run

```bash
python assignment_python_24.py
```

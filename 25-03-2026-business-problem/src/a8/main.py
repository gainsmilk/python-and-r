# task 1: student info
name = "Draedon"
age = 17
grade = 4.5
print(f"{name} is {age} years old and has a grade of {grade}")

# task 2: math operations
a = 15
b = 4
print(f"Integer division: {a // b}")
print(f"Remainder: {a % b}")
print(f"Power: {a ** b}")
print(str(a // b) + " students per group")

# task 3: subjects list
subjects = ["Math", "English", "Physics", "History"]
print(f"First: {subjects[0]}")
print(f"Last: {subjects[-1]}")

subjects.append("Computer Science")
subjects.remove("English")

counter = 1
for subject in subjects:
    print(f"{counter}. {subject}")
    counter += 1

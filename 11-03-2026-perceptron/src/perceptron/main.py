x1 = int(input("Is the gym open? (1-yes, 0-no): "))  # is the gym open? (yes)
# IMPORTANCE: gym being open is critical
w1 = int(input("How important is gym being open? (1-5): "))

x2 = int(input("Did you sleep well? (1-yes, 0-no): "))  # did i sleep well? (no)
# IMPORTANCE: sleep matters the most for performance
w2 = int(input("How important is sleep for performance? (1-5): "))

x3 = int(input("Do you have pre-workout? (1-yes, 0-no): "))  # do i have pre-workout? (yes)
# IMPORTANCE: pre-workout helps but not mandatory
w3 = int(input("How important is pre-workout? (1-5): "))

threshold = int(input("Threshold value: "))

total = x1 * w1 + x2 * w2 + x3 * w3
output = 1 if total > threshold else 0

print(f"Weighted sum: {total}")
print(f"Go to the gym: {'yes' if output == 1 else 'no'}")

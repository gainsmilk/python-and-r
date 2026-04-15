"""Python 18 assignment: simple bench press 1RM calculator."""

from __future__ import annotations


def epley_one_rm(weight: float, reps: int) -> float:
    """Estimates 1RM using the Epley formula.

    Args:
        weight: Weight lifted in kg.
        reps: Number of reps performed.

    Returns:
        Estimated 1RM in kg.
    """

    return weight * (1 + reps / 30)


def brzycki_one_rm(weight: float, reps: int) -> float:
    """Estimates 1RM using the Brzycki formula.

    Args:
        weight: Weight lifted in kg.
        reps: Number of reps performed.

    Returns:
        Estimated 1RM in kg.
    """

    return weight * 36 / (37 - reps)


def rating(one_rm: float) -> str:
    """Returns a simple lift rating for a 1RM value in kg."""

    if one_rm < 60:
        return "beginner"
    if one_rm < 100:
        return "intermediate"
    if one_rm < 140:
        return "advanced"
    return "elite"


def main() -> None:
    """Runs the 1RM calculator."""

    name = input("Your name: ").strip()
    exercise = input("Exercise (e.g. bench press): ").strip()
    weight_input = input("Weight lifted in kg: ")
    reps_input = input("Reps: ")

    weight = float(weight_input)
    reps = int(reps_input)

    if reps <= 0 or reps > 20:
        print("Reps must be between 1 and 20 for a reliable estimate.")
        return

    greeting = "hi " + name[:3].upper() + ", lets see your numbers."
    print(greeting)

    formulas = ["epley", "brzycki"]
    results: list[float] = []

    for formula in formulas:
        if formula == "epley":
            value = epley_one_rm(weight, reps)
        else:
            value = brzycki_one_rm(weight, reps)
        results.append(round(value, 1))

    results.sort()
    average = sum(results) / len(results)

    print(f"{exercise.title()} 1RM estimates: {results[0]} kg - {results[-1]} kg")
    print(f"Average: {round(average, 1)} kg ({rating(average)})")


if __name__ == "__main__":
    main()

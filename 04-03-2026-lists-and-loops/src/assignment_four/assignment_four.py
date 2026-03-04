"""Assignment 4 solution: conditions and user input."""

from __future__ import annotations


def get_temperature_message(temperature: float) -> str:
    """Returns the freezing status message for a temperature value.

    Args:
        temperature: Entered temperature as a number.

    Returns:
        Message describing whether it is freezing or above freezing.
    """

    if temperature < 0:
        return "It is freezing."
    return "It is above freezing."


def get_exam_result_message(score: int) -> str:
    """Returns exam pass/fail message based on score.

    Args:
        score: Exam score in range 0-100.

    Returns:
        Pass/fail message.

    Raises:
        ValueError: If score is outside the 0-100 range.
    """

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 50:
        return "You passed the exam."
    return "You failed the exam."


def main() -> None:
    """Runs Assignment 4 tasks in order."""

    temperature_input = input("Enter the temperature: ")
    temperature = float(temperature_input)
    print(get_temperature_message(temperature))

    score_input = input("Enter your exam score (0-100): ")
    score = int(score_input)
    print(get_exam_result_message(score))


if __name__ == "__main__":
    main()

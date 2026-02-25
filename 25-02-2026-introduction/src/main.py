"""Assignment 1 solution for Python syntax and variables."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class VariableBinding[T]:
    """Stores a named variable binding.

    Attributes:
        name: Human-readable variable name.
        value: Runtime value assigned to the variable.
    """

    name: str
    value: T


def format_type_line(binding: VariableBinding[Any]) -> str:
    """Formats one variable type report line.

    Args:
        binding: Variable binding that should be reported.

    Returns:
        A printable line containing the variable name and its runtime type.
    """

    return f"{binding.name}: {type(binding.value)}"


def swap_values[T, U](left: T, right: U) -> tuple[U, T]:
    """Swaps two values without a temporary variable.

    Args:
        left: Left-hand value.
        right: Right-hand value.

    Returns:
        A tuple containing the values in swapped order.
    """

    left, right = right, left
    return left, right


def main() -> None:
    """Runs assignment output in order."""

    print("Hello, Python!")

    # The # symbol starts a comment, and Python ignores comment text.
    integer_value = 11
    float_value = 11.11
    string_value = "Python"

    bindings = (
        VariableBinding("integer_value", integer_value),
        VariableBinding("float_value", float_value),
        VariableBinding("string_value", string_value),
    )

    for line in map(format_type_line, bindings):
        print(line)

    left_name = "alpha"
    right_name = "beta"
    print(f"before swap: left_name={left_name}, right_name={right_name}")
    left_name, right_name = swap_values(left_name, right_name)
    print(f"after swap: left_name={left_name}, right_name={right_name}")


if __name__ == "__main__":
    main()

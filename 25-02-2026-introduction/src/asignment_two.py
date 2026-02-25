"""Assignment 2 solution for data types and operators."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from operator import add, floordiv, mod, mul, sub, truediv
from typing import Any

type Number = int | float
type BinaryOperator = Callable[[int, int], Number]


class ArithmeticSymbol(StrEnum):
    """Supported arithmetic operation symbols."""

    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    FLOOR_DIVIDE = "//"
    MODULO = "%"


OPERATOR_REGISTRY: dict[ArithmeticSymbol, BinaryOperator] = {
    ArithmeticSymbol.ADD: add,
    ArithmeticSymbol.SUBTRACT: sub,
    ArithmeticSymbol.MULTIPLY: mul,
    ArithmeticSymbol.DIVIDE: truediv,
    ArithmeticSymbol.FLOOR_DIVIDE: floordiv,
    ArithmeticSymbol.MODULO: mod,
}


@dataclass(frozen=True, slots=True)
class ArithmeticEvaluation:
    """Represents one arithmetic result."""

    expression: str
    value: Number


@dataclass(frozen=True, slots=True)
class TruthinessEvaluation:
    """Represents one truthiness result."""

    raw_value: Any
    result: bool


def evaluate_arithmetic(x: int, y: int) -> tuple[ArithmeticEvaluation, ...]:
    """Evaluates the configured arithmetic operations for x and y.

    Args:
        x: Left operand.
        y: Right operand.

    Returns:
        Tuple of structured arithmetic evaluations.
    """

    return tuple(
        ArithmeticEvaluation(
            expression=f"{x} {symbol.value} {y}",
            value=operator_fn(x, y),
        )
        for symbol, operator_fn in OPERATOR_REGISTRY.items()
    )


def concatenate_integer(value: int, suffix: str) -> str:
    """Converts an integer to string and concatenates it with a suffix.

    Args:
        value: Integer to convert.
        suffix: String content to append.

    Returns:
        Concatenated string.
    """

    return str(value) + suffix


def evaluate_truthiness(values: tuple[Any, ...]) -> tuple[TruthinessEvaluation, ...]:
    """Evaluates boolean truthiness for a tuple of values.

    Args:
        values: Values to test with bool().

    Returns:
        Tuple of truthiness evaluations.
    """

    return tuple(
        TruthinessEvaluation(raw_value=value, result=bool(value)) for value in values
    )


def main() -> None:
    """Runs Assignment 2 tasks."""

    x, y = 10, 3
    print("Arithmetic operations:")
    for evaluation in evaluate_arithmetic(x=x, y=y):
        print(f"{evaluation.expression} = {evaluation.value}")

    concatenated = concatenate_integer(10, " is now text")
    print(f"\nString concatenation:\n{concatenated}")

    values_to_check = (0, "", "Python", -5)
    print("\nTruthiness checks:")
    for evaluation in evaluate_truthiness(values_to_check):
        print(f"bool({evaluation.raw_value!r}) = {evaluation.result}")


if __name__ == "__main__":
    main()

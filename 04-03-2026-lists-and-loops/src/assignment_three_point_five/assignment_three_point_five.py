"""Assignment 3.5 suggested solution: lists and loops."""

from __future__ import annotations


def create_cities() -> list[str]:
    """Creates the initial cities list.

    Returns:
        A list containing five city names.
    """

    return ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"]


def print_city_access_examples(cities: list[str]) -> None:
    """Prints required access examples for the list.

    Args:
        cities: Source list of city names.

    Raises:
        ValueError: If the list has fewer than three items.
    """

    if len(cities) < 3:
        raise ValueError("At least three cities are required.")

    print(f"Third city: {cities[2]}")
    print(f"First city via negative indexing: {cities[-len(cities)]}")


def update_cities(cities: list[str], new_city: str) -> list[str]:
    """Adds a city and removes the last city.

    Args:
        cities: Source list of city names.
        new_city: City name to add.

    Returns:
        Updated list after adding a city and removing the last city.
    """

    updated_cities = cities.copy()
    updated_cities.insert(0, new_city)
    updated_cities.pop()
    return updated_cities


def print_cities_with_for_loop(cities: list[str]) -> None:
    """Prints each city with a for loop.

    Args:
        cities: List of city names.
    """

    print("Cities list:")
    for city in cities:
        print(f"- {city}")


def print_numbers_with_while_loop(start: int = 5, end: int = 15) -> None:
    """Prints numbers from start to end with a while loop.

    Args:
        start: Starting number.
        end: Final number.
    """

    print("Numbers from 5 to 15:")
    current_number = start
    while current_number <= end:
        print(current_number)
        current_number += 1


def main() -> None:
    """Runs the full assignment flow."""

    cities = create_cities()
    print_city_access_examples(cities)

    cities = update_cities(cities, "Edmonton")
    print(f"Updated cities: {cities}")

    print_cities_with_for_loop(cities)
    print_numbers_with_while_loop()


if __name__ == "__main__":
    main()

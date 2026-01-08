#!/usr/bin/env python3


def garden_operations() -> None:
    """Demonstrate various error types."""
    print("Testing ValueError...")
    int("abc")

    print("Testing ZeroDivisionError...")
    print(10/0)

    print("Testing FileNotFoundError...")
    open("missing.txt")

    print("Testing KeyError...")
    plant = {
        "name": "Rose",
        "height": 15
    }
    print(plant["age"])


def test_error_types() -> None:
    """Test and catch different error types."""
    try:
        print("Testing ValueError...")
        int("abc")

    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("")

    try:
        print("Testing ZeroDivisionError...")
        print(10/0)

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("")

    try:
        print("Testing KeyError...")
        plant = {
            "name": "Rose",
            "height": 15
            }
        print(plant["missing_plant"])

    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("")

    try:
        print("Testing multiple errors together...")
        int("abc")
        print(10/0)
        open("missing.txt")
        garden = {"plant1": "Rose"}
        print(garden["plant1"])

    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


print("=== Garden Error Types Demo ===")

print("")

test_error_types()

print("")

print("All error types tested successfully!")

#!/usr/bin/env python3


def check_temperature(temp_str: str) -> str:
    """Check if temperature is safe for plants."""
    try:
        print(f"Testing temperature: {temp_str}")
        temperature = int(temp_str)

        if temperature < 0:
            return f"Error: {temperature}°C is too cold for plants (min 0°C)"

        elif temperature > 40:
            return f"Error: {temperature}°C is too hot for plants (max 40°C)"

        else:
            return f"Temperature {temperature}°C is perfect for plants!"

    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    print(check_temperature("25"))
    print("")

    print(check_temperature("abc"))
    print("")

    print(check_temperature("100"))
    print("")

    print(check_temperature("-50"))
    print("")

    print("All tests completed - program didn't crash!")


test_temperature_input()

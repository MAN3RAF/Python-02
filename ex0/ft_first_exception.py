#!/usr/bin/env python3


def check_temperature(temp_str: str) -> None:
    """Check if temperature is safe for plants."""
    try:
        print(f"Testing temperature: {temp_str}")
        temperature = int(temp_str)

        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")

        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")

        else:
            print(f"Temperature {temperature}°C is perfect for plants!")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


print("=== Garden Temperature Checker ===")

print("")

check_temperature("25")

print("")

check_temperature("abc")

print("")

check_temperature("100")

print("")

check_temperature("-50")

print("")

print("All tests completed - program didn't crash!")

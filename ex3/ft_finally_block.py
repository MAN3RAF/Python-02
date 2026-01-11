#!/usr/bin/env python3


def water_plants(plant_list: list) -> None:
    """Water plants with cleanup."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or not isinstance(plant, str):
                raise ValueError("Cannot water None - invalid plant!")

            print(f"Watering {plant}")

    except ValueError:
        print("Error: Cannot water None - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system."""
    good_list = ["tomato", "lettuce", "carrots"]

    bad_list = ["tomato", None]

    print("Testing normal watering...")

    water_plants(good_list)

    print("Watering completed successfully!")

    print("")

    print("Testing with error...")

    water_plants(bad_list)


print("=== Garden Watering System ===")

print("")

test_watering_system()

print("")

print("Cleanup always happens, even with errors!")

#!/usr/bin/env python3

def water_plants(plant_list):
	
	try:
		print("Opening watering system")
		for plant in plant_list:
			"""
			if plant is str it will water if not it will cause
			an error because .lower() doesnt work on none str
			"""
			if not isinstance(plant, str):
				plant.lower()
			
			print(f"Watering {plant}")

	except:
		print("Error: Cannot water None - invalid plant!")

	finally:
		print("Closing watering system (cleanup)")


def test_watering_system():

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

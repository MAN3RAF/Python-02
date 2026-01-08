#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
	
	try:
		if not plant_name:
			raise ValueError("Error: Plant name cannot be empty!")
		elif water_level > 10:
			raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
		elif water_level < 1:
			raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
		elif sunlight_hours < 2:
			raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
		elif sunlight_hours > 12:
			raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
		else:
			return f"Plant '{plant_name}' is healthy!"
		
	except ValueError as Error:
		print(f"{Error}")


def test_plant_checks():

	print("Testing good values...")
	print(check_plant_health("tomato", 5, 5))

	print("")

	print("Testing empty plant name...")
	check_plant_health("", 5, 5)

	print("")

	print("Testing bad water level...")
	check_plant_health("tomato", 15, 5)

	print("")

	print("Testing bad sunlight hours...")
	check_plant_health("tomato", 5, 0)


print("=== Garden Plant Health Checker ===")

print("")

test_plant_checks()

print("")

print("All error raising tests completed!")

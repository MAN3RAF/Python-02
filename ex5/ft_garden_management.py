#!/usr/bin/env python3

class GardenError(Exception):
	pass


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


class GardenManager:

	
	def add_plants(plants):
		print("Adding plants to garden...")
		for plant in plants:
			try:
				if not plant:
					raise PlantError("Error adding plant: Plant name cannot be empty!")
				else:
					print(f"Added {plant} successfully")

			except PlantError as e:
				print(e)

	def water_plants(plants, water_level):
		print("Watering plants...")
		print("Opening watering system")
		try:
			for plant in 
		
		except:
			pass

	def check_planthealth(plants, water_level, sunlight_hours):
		pass


print("=== Garden Management System ===")

print("")

plants = ["tomato", "lettuce", ""]

manager = GardenManager

manager.add_plants(plants)

print("")



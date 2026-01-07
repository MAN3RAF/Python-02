#!/usr/bin/env python3

class GardenError(Exception):
    '''Base class for all garden Errors'''
    pass


class PlantError(GardenError):
    '''Error class thats related to Plant Errors'''
    pass


class WaterError(GardenError):
    """Error class thats related to Water problems"""
    pass


print("=== Custom Garden Errors Demo ===")

print("")

print("Testing PlantError...")
try:
    raise PlantError("The tomato plant is wilting!")

except PlantError as e:
    print(f"Caught PlantError: {e}")

print("")

print("Testing WaterError...")
try:
    raise WaterError("Not enough water in the tank!")

except WaterError as e:
    print(f"Caught WaterError: {e}")

print("")

print("Testing catching all garden errors...")
try:
    raise PlantError("The tomato plant is wilting!")

except GardenError as e:
    print(f"Caught a garden error: {e}")

try:
    raise WaterError("Not enough water in the tank!")

except GardenError as e:
    print(f"Caught a garden error: {e}")

print("")

print("All custom error types work correctly!")

#!/usr/bin/env python3

def garden_operations():

	#Testing ValueError
	print("Testing ValueError...")
	x = int("abc")
	
	#Testing ZeroDivisionError
	print("Testing ZeroDivisionError...")
	print(10/0)

	#Testing FileNotFoundError
	print("Testing FileNotFoundError...")
	open("unknown.txt")

	#Testing KeyError
	print("Testing KeyError...")
	plant = {
		"name": "Rose",
		"height": 15
	}
	print(plant["age"])


def test_error_types():

	try:
		print("Testing ValueError...")
		x = int("abc")

	except ValueError:
		print("Caught ValueError: invalid literal for int()")

	try:
		print("\nTesting ZeroDivisionError...")
		print(10/0)

	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero")

	try:
		print("\nTesting FileNotFoundError...")
		open("unknown.txt")

	except FileNotFoundError:
		print("Caught FileNotFoundError: No such file 'missing.txt'")

	try:
		print("\nTesting KeyError...")
		plant = {
			"name": "Rose",
			"height": 15
			}
		print(plant["age"])

	except KeyError:
		print("Caught KeyError: 'missing\_plant'")

	try:
		print("\nTesting multiple errors together...")
		x = int("abc")
		print(10/0)
		open("unknown.txt")
		garden = {"plant1": "Rose"}
		print(garden["plant1"])
	
	except (ValueError, ZeroDivisionError, FileNotFoundError ,KeyError):
		print("Caught an error, but program continues!")


print("=== Garden Error Types Demo ===")

print("")

test_error_types()

print("")

print("All error types tested successfully!")

import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate required values using the math module
square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (logarithm not defined for non-positive numbers)"
sine_value = math.sin(num)

# Display the results
print(f"Square root of {num}: {square_root}")
print(f"Natural logarithm of {num}: {natural_log}")
print(f"Sine of {num} (in radians): {sine_value}")

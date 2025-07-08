# Basic numeric types
x = 10       # Integer
y = 3.5      # Float

# Arithmetic operations
sum_total = x + y
difference = x - y
product = x * y
quotient = x / y
power = x ** 2
modulus = x % 3

print("Sum:", sum_total)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Power:", power)
print("Modulus:", modulus)

# Type conversion
z = "100"
converted = int(z) + x
print("Converted sum:", converted)

# Using math module
import math

print("Square root of x:", math.sqrt(x))
print("Floor of y:", math.floor(y))
print("Ceiling of y:", math.ceil(y))
print("Random number between 1 and 100:", math.floor(math.pi * 31))  # Just for fun!

# Working with lists of numbers
numbers = [5, 3, 9, 1, 6]
average = sum(numbers) / len(numbers)
print("Average:", average)


# Numeric variables
a = 15
b = 4

# Arithmetic Operators
print("Addition:", a + b)           
print("Subtraction:", a - b)       
print("Multiplication:", a * b)    
print("Division:", a / b)           
print("Floor Division:", a // b)
print("Modulus (remainder):", a % b)  
print("Exponentiation:", a ** b)    

# Comparison Operators
print("Is a equal to b?", a == b)
print("Is a greater than b?", a > b)
print("Is a not equal to b?", a != b)

# Assignment Operators
c = 10
c += 5  # Same as: c = c + 5
print("Value of c after += 5:", c)

# Logical Operators
is_even = (a % 2 == 0)
is_large = (a > 10)
print("Is a even AND large?", is_even and is_large)
print("Is a even OR large?", is_even or is_large)

# Bitwise Operators (just for fun)
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)


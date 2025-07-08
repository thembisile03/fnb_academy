# This function prints a friendly greeting
def say_hello(name):
    print("Hello, (name).")

# Call the function
say_hello("Thembi")

# This function adds two numbers and returns the result
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Calling the function with example values
sum_result = add_numbers(5, 3)
print("The sum is:", sum_result)

def calculate_factorial(number):
    # Check if the number is negative, zero, or positive
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif number == 0:
        print("The factorial of 0 is 1.")
    else:
        factorial = 1
        # Loop from 1 to the number
        for i in range(1, number + 1):
            factorial *= i
        print("The factorial of", number, "is", factorial)

# Try it out with different values
calculate_factorial(5)
calculate_factorial(0)
calculate_factorial(-3)



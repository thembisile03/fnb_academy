# Create a student gradebook using a dictionary
gradebook = {
    "Alice": 85,
    "Brian": 92,
    "Cleo": 78
}

# Add a new student
gradebook["Dylan"] = 88

# Update a grade
gradebook["Alice"] = 90  # Alice improved her score!

# Delete a student (maybe they moved)
del gradebook["Cleo"]

# Print each student's grade
for student, grade in gradebook.items():
    print(f"{student}: {grade}")


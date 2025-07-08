# Original strings
first_name = "Thembi"
last_name = "Mthimunye"

# Concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Repetition
echo = (first_name + "! ") * 3
print("Echo:", echo)

# Slicing
print("First three letters of last name:", last_name[:3])

# Replace
greeting = "Hello ekasi"
new_greeting = greeting.replace("ekasi", "Thembi")
print("Personalized Greeting:", new_greeting)

# Checking content
print("Does greeting contain 'Hello'?","Hello" in greeting)

# Stripping whitespace
messy = "  python is awesome  "
clean = messy.strip()
print("Cleaned text:", clean)

# Capitalizing
print("Title Case:", full_name.title())
print("Upper Case:", full_name.upper())
print("Lower Case:", full_name.lower())


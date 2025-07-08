
# Multiline and escaped strings
quote = "She said, \"Python's awesome!\"\nLet's level up your skills."
print(quote)

# String slicing
word = "ekasination"
print(word[2:6])       # prints 'asin'
print(word[::-1])      # reverses the string

# Using join, split, and replace
sentence = "Python is powerful and fun"
words = sentence.split()         # Turns into a list of words
joined = "-".join(words)         # Joins words with dashes
print(joined)

# Replace certain words
new_sentence = sentence.replace("fun", "super fun")
print(new_sentence)

# Advanced formatting
name = "Thembi"
language = "Python"
level = "intermediate"

formatted = f"{name:^10} | {language.upper():<10} | {level.title():>15}"
print(formatted)

# String testing methods
code = "Abc123"
print(code.isalnum())    # True: only letters and numbers
print(code.isalpha())    # False: contains numbers

# Encoding and decoding
encoded = "Molo ekasi".encode("utf-8")
print(encoded)
decoded = encoded.decode("utf-8")
print(decoded)


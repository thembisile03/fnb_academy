# Defining a tuple of nuts
nuts = ("Almond", "Cashew", "Pistachio", "Walnut", "Hazelnut")

# Accessing elements in a tuple
print("First nut in the list:", nuts[0])
print("Last nut in the list:", nuts[-1])

# Looping through the tuple
print("\nAll the nuts in the tuple:")
for nut in nuts:
    print("-", nut)

# Checking for membership
if "Cashew" in nuts:
    print("\nYes! Cashew is part of the tuple.")

# Getting the length of the tuple
print("\nTotal number of nuts:", len(nuts))


# List of different types of nuts
nuts = ["Almond", "Cashew", "Pistachio", "Walnut", "Hazelnut", "Macadamia"]

# Print each nut in the list
print("Here's a list of delicious nuts:")
for nut in nuts:
    print(f"- {nut}")

# Add a new nut to the list
nuts.append("Pecan")
print("\nAdded a new nut! Here's the updated list:")
print(nuts)

# Sort the list alphabetically
nuts.sort()
print("\nSorted list of nuts:")
print(nuts)

# Check if a specific nut is in the list
search_nut = "Cashew"
if search_nut in nuts:
    print(f"\nYes! {search_nut} is in the list.")
else:
    print(f"\nNope, {search_nut} is not in the list.")

# Initial list of nuts
nuts = ["Almond", "Cashew", "Pistachio", "Walnut"]

print("Original list of nuts:")
print(nuts)

# Using insert() to add a nut at a specific index
nuts.insert(2, "Macadamia")
print("\nAfter inserting 'Macadamia' at index 2:")
print(nuts)

# Using remove() to delete a nut from the list
nuts.remove("Walnut")
print("\nAfter removing 'Walnut':")
print(nuts)

# Using sort() to arrange the list in alphabetical order
nuts.sort()
print("\nAfter sorting the list alphabetically:")
print(nuts)


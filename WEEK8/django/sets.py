# Creating a set of nuts
nut_set = {"Almond", "Cashew", "Pistachio", "Walnut", "Hazelnut"}

print("Original set of nuts:")
print(nut_set)

# Adding a new nut to the set
nut_set.add("Macadamia")
print("\nAfter adding 'Macadamia':")
print(nut_set)

# Removing a nut from the set
nut_set.remove("Walnut")
print("\nAfter removing 'Walnut':")
print(nut_set)

# Checking if a nut is in the set
if "Cashew" in nut_set:
    print("\nCashew is still in the set!")

# Creating another set for demonstration
more_nuts = {"Brazil Nut", "Cashew", "Pine Nut"}

# Finding the intersection of the two sets
common_nuts = nut_set.intersection(more_nuts)
print("\nNuts in both sets:", common_nuts)

# Union of both sets
all_nuts = nut_set.union(more_nuts)
print("\nCombined set of all nuts:")
print(all_nuts)


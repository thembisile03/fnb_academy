# Initial stock levels
stock = {
    "pens": 100,
    "notebooks": 50,
    "erasers": 30
}

# Sell some items (use subtraction)
stock["pens"] -= 15   # Sold 15 pens
stock["notebooks"] -= 10  # Sold 10 notebooks

# Restock some items (use addition)
stock["erasers"] += 20  # Added 20 erasers

# Calculate total items using addition
total_items = stock["pens"] + stock["notebooks"] + stock["erasers"]

# Compare two stock levels (use comparison operators)
more_pens_than_notebooks = stock["pens"] > stock["notebooks"]

# Display updated stock and results
print("Updated Stock:")
for item, quantity in stock.items():
    print(f"{item.capitalize()}: {quantity}")

print("\nTotal Items in Stock:", total_items)
print("More pens than notebooks?", more_pens_than_notebooks)


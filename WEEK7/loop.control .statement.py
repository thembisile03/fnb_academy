vegetables = ["carrot", "broccoli", "spinach", "onion", "pepper", "potato"]

for veg in vegetables:
    if veg == "onion":
        print("Skipping onion... too many tears!")
        continue  # Skip onion

    if veg == "pepper":
        print("Found pepper! That’s spicy enough for today.")
        break  # Stop the loop when we find pepper

    print(f"Adding {veg} to the salad.")


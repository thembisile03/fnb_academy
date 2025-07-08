vegetables = ["carrot", "tomato", "cucumber", "lettuce", "pumpkin"]
quantities = [3, 5, 2, 1, 4]

print("Let's fill the veggie basket!")

for i in range(len(vegetables)):
    veg = vegetables[i]
    qty = quantities[i]
    print(f"Adding {qty} {veg}(s) to the basket.")


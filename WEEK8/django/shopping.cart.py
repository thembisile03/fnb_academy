class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store item: quantity
        self.categories = set()  # Set to track unique item categories

    def add_item(self, name, quantity, category="general"):
        name = name.strip().title()  # String methods
        self.categories.add(category.lower())
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"🛒 Added {quantity} x {name}")

    def remove_item(self, name):
        name = name.strip().title()
        if name in self.items:
            del self.items[name]
            print(f"❌ Removed {name}")
        else:
            print(f"{name} not found in cart.")

    def update_quantity(self, name, quantity):
        name = name.strip().title()
        if name in self.items:
            self.items[name] = quantity
            print(f"🔄 Updated {name} to {quantity}")
        else:
            print(f"{name} not in cart.")

    def show_cart(self):
        if not self.items:
            print("Your cart is empty!")
            return
        print("\n🧺 Your Shopping Cart:")
        for item, qty in self.items.items():
            print(f"- {item}: {qty}")
        print(f"Categories in cart: {', '.join(sorted(self.categories))}")

    def clear_cart(self):
        self.items.clear()
        self.categories.clear()
        print("🧹 Cart has been cleared.")

# --- Example usage ---
cart = ShoppingCart()
cart.add_item("apples", 4, "fruits")
cart.add_item("milk", 1, "dairy")
cart.add_item("bread", 2, "bakery")
cart.show_cart()
cart.update_quantity("milk", 3)
cart.remove_item("bread")
cart.show_cart()
cart.clear_cart()
cart.show_cart()


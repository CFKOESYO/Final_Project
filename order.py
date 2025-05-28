class Order:
    def __init__(self):
        self.items = []  

    def add_item(self, item, quantity):
        self.items.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity,
            "subtotal": item["price"] * quantity
        })

    def display_order(self):
        if not self.items:
            print("Your order is currently empty.")
            return

        print("\nCurrent Order:")
        total = 0
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['name']} x{item['quantity']} - ${item['subtotal']:.2f}")
            total += item['subtotal']
        print(f"Total: ${total:.2f}")

    def get_total(self):
        return sum(item['subtotal'] for item in self.items)

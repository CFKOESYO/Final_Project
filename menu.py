MENU = {
    1: {"name": "Burger", "price": 5.00},
    2: {"name": "Fries", "price": 2.50},
    3: {"name": "Cola", "price": 1.50},
    4: {"name": "Fried Chicken", "price": 6.00}
}

def display_menu():
    print("\nMENU")
    for key, item in MENU.items():
        print(f"{key}. {item['name']} - ${item['price']:.2f}")
    print("5. Checkout and Exit")
from menu import MENU, display_menu
from order import Order

def main():
    print("Welcome to the fast food restaurant.")
    order = Order()

    while True:
        display_menu()
        try:
            choice = int(input("\nEnter menu number (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 5:
            print("\nFinalizing your order...")
            order.display_order()
            print("Thank you for your visit!")
            break
        elif choice in MENU:
            try:
                qty = int(input(f"Enter quantity for {MENU[choice]['name']}: "))
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
            except ValueError:
                print("Please enter a valid quantity number.")5
                
                continue

            order.add_item(MENU[choice], qty)
            print(f"Added {qty} x {MENU[choice]['name']} to your order.")
        else:
            print("Invalid menu choice. Please try again.")

if __name__ == '__main__':
    main()
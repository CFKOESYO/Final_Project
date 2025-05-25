# Final_Project
# Fast Food Restaurant Ordering System (Python)

This is a simple terminal-based ordering system written in Python. It simulates the basic ordering process in a fast food restaurant, supporting menu display, quantity input, price calculation, subtotal and total amount computation, and checkout.

---

## Features

- Display a predefined menu with prices
- Allow customers to input item quantity
- Validate numeric input and handle errors
- Automatically calculate subtotal (quantity × price)
- Show current order details and total cost
- Gracefully exit with a thank-you message

---

## Example Output

Welcome to the Fast Food Ordering System!

MENU

Burger - $5.00

Fries - $2.50

Cola - $1.50

Fried Chicken - $6.00

Checkout and Exit

Enter menu number (1-5): 1
Enter quantity for Burger: 2
Added 2 x Burger to your order.

Enter menu number (1-5): 3
Enter quantity for Cola: 3
Added 3 x Cola to your order.

Enter menu number (1-5): 5

Finalizing your order...

Burger x2 - $10.00

Cola x3 - $4.50
Total: $14.50

Thank you for your visit!

---

## Project Structure
fastfood_ordering/
├── main.py # Main entry point of the program
├── menu.py # Menu data and display logic
├── order.py # Order management: add, display, calculate
└── README.md # Project description

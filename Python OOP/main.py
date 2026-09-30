"""
============================================================
 KUSINA DE CANONIGO - RESTAURANT ORDERING SYSTEM (PYTHON OOP)
============================================================
"""

from order import Order

menu = {
    "Pork Adobo": 120.00,
    "Chicken Adobo": 110.00,
    "Kaldereta": 130.00,
    "Sinigang": 125.00,
    "Grilled Bangus": 140.00
}


def main():
    print("Welcome to KUSINA DE CANONIGO Ordering System!\n")

    order = Order(menu)
    order.display_menu()

    print()
    if not Order.ask_yes_no("Would you like to place an order?"):
        print("\nThank you for visiting KUSINA DE CANONIGO. Come back soon!")
        return

    print()
    order.take_order()
    order.calculate_order()

    print()
    order.apply_discount()
    order.print_receipt()


if __name__ == "__main__":
    main()

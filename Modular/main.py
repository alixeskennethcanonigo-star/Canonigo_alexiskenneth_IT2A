"""
============================================================
 KUSINA DE CANONIGO - RESTAURANT ORDERING SYSTEM (MODULAR)
============================================================
"""

from menu import menu, display_menu
from inputs import ask_yes_no
from order import take_order, calculate_order
from discount import apply_discount
from receipt import print_receipt


def main():
    print("Welcome to KUSINA DE CANONIGO Ordering System!\n")

    display_menu(menu)

    print()
    wants_to_order = ask_yes_no("Would you like to place an order?")

    if not wants_to_order:
        print("\nThank you for visiting KUSINA DE CANONIGO. Come back soon!")
        return

    print()
    customer_order = take_order(menu)

    item_subtotals, order_total = calculate_order(menu, customer_order)

    print()
    discount_amount, discount_label = apply_discount(order_total)

    print_receipt(menu, customer_order, item_subtotals, order_total, discount_amount, discount_label)


if __name__ == "__main__":
    main()

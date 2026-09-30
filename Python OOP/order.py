"""order.py - the Order class for KUSINA DE CANONIGO."""

import datetime


class Order:
    """One customer's order.

    Attributes: menu, items, subtotals, total, discount_amount, discount_label
    Methods:    display_menu, take_order, calculate_order, apply_discount, print_receipt
    """

    def __init__(self, menu):
        self.menu = menu
        self.items = {}
        self.subtotals = {}
        self.total = 0.00
        self.discount_amount = 0.00
        self.discount_label = "None"

    # ---------- input helpers ----------
    @staticmethod
    def ask_yes_no(question):
        while True:
            answer = input(question + " (yes/no): ").strip().lower()
            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print(">> Invalid input. Please type 'yes' or 'no'.\n")

    def get_menu_item(self):
        while True:
            item_name = input("Enter the menu item you want to order: ").strip().title()
            if item_name in self.menu:
                return item_name
            else:
                print(">> Sorry, that item is not on the menu. Please try again.\n")

    @staticmethod
    def get_quantity(item_name):
        while True:
            qty_input = input(f"Enter quantity for {item_name}: ").strip()
            if qty_input.isdigit() and int(qty_input) > 0:
                return int(qty_input)
            else:
                print(">> Invalid quantity. Please enter a positive whole number.\n")

    # ---------- behaviors ----------
    def display_menu(self):
        print("=" * 46)
        print("            KUSINA DE CANONIGO - MENU")
        print("=" * 46)
        print(f"{'MENU ITEM':<25}{'PRICE (PHP)':>18}")
        print("-" * 46)
        for item, price in self.menu.items():
            print(f"{item:<25}{price:>15.2f}")
        print("=" * 46)

    def take_order(self):
        while True:
            item_name = self.get_menu_item()
            quantity = self.get_quantity(item_name)

            if item_name in self.items:
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity

            print(f">> Added {quantity} x {item_name} to your order.\n")

            if not self.ask_yes_no("Would you like to order another item?"):
                break

    def calculate_order(self):
        self.subtotals = {}
        self.total = 0.00

        for item_name, quantity in self.items.items():
            subtotal = self.menu[item_name] * quantity
            self.subtotals[item_name] = subtotal
            self.total += subtotal

    def apply_discount(self):
        self.discount_amount = 0.00
        self.discount_label = "None"

        is_senior_or_pwd = self.ask_yes_no("Are you a Senior Citizen or PWD?")

        if is_senior_or_pwd:
            self.discount_amount = self.total * 0.20
            self.discount_label = "Senior Citizen / PWD Discount (20%)"
        elif self.total >= 500:
            self.discount_amount = self.total * 0.10
            self.discount_label = "Loyalty Discount for orders >= PHP 500 (10%)"

    def print_receipt(self):
        now = datetime.datetime.now().strftime("%B %d, %Y  %I:%M %p")

        print("\n")
        print("=" * 46)
        print("            KUSINA DE CANONIGO".center(46))
        print("      Authentic Filipino Home Cooking".center(46))
        print("=" * 46)
        print(f" Date: {now}")
        print("-" * 46)
        print(f"{'ITEM':<16}{'QTY':>5}{'PRICE':>10}{'SUBTOTAL':>15}")
        print("-" * 46)

        for item_name, quantity in self.items.items():
            price = self.menu[item_name]
            subtotal = self.subtotals[item_name]
            print(f"{item_name:<16}{quantity:>5}{price:>10.2f}{subtotal:>15.2f}")

        print("-" * 46)
        print(f"{'SUBTOTAL':<31}{self.total:>15.2f}")

        if self.discount_amount > 0:
            print(f"{self.discount_label:<31}{'-' + format(self.discount_amount, '.2f'):>15}")

        final_total = self.total - self.discount_amount
        print("-" * 46)
        print(f"{'TOTAL AMOUNT DUE':<31}{final_total:>15.2f}")
        print("=" * 46)
        print("      Thank you for dining with us!".center(46))
        print("         Salamat po at Kain Tayo!".center(46))
        print("=" * 46)

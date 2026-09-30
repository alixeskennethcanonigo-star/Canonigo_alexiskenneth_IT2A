"""receipt.py - prints the final receipt."""

import datetime


def print_receipt(menu_dict, order_dict, subtotals, total, discount_amount, discount_label):
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

    for item_name, quantity in order_dict.items():
        price = menu_dict[item_name]
        subtotal = subtotals[item_name]
        print(f"{item_name:<16}{quantity:>5}{price:>10.2f}{subtotal:>15.2f}")

    print("-" * 46)
    print(f"{'SUBTOTAL':<31}{total:>15.2f}")

    if discount_amount > 0:
        print(f"{discount_label:<31}{'-' + format(discount_amount, '.2f'):>15}")

    final_total = total - discount_amount
    print("-" * 46)
    print(f"{'TOTAL AMOUNT DUE':<31}{final_total:>15.2f}")
    print("=" * 46)
    print("      Thank you for dining with us!".center(46))
    print("         Salamat po at Kain Tayo!".center(46))
    print("=" * 46)

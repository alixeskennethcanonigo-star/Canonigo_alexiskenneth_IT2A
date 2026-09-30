"""menu.py - holds the menu data and displays it."""

menu = {
    "Pork Adobo": 120.00,
    "Chicken Adobo": 110.00,
    "Kaldereta": 130.00,
    "Sinigang": 125.00,
    "Grilled Bangus": 140.00
}


def display_menu(menu_dict):
    print("=" * 46)
    print("            KUSINA DE CANONIGO - MENU")
    print("=" * 46)
    print(f"{'MENU ITEM':<25}{'PRICE (PHP)':>18}")
    print("-" * 46)
    for item, price in menu_dict.items():
        print(f"{item:<25}{price:>15.2f}")
    print("=" * 46)

"""order.py - takes the customer's order and computes the totals."""

from inputs import ask_yes_no, get_menu_item, get_quantity


def take_order(menu_dict):
    order = {}

    while True:
        item_name = get_menu_item(menu_dict)
        quantity = get_quantity(item_name)

        if item_name in order:
            order[item_name] += quantity
        else:
            order[item_name] = quantity

        print(f">> Added {quantity} x {item_name} to your order.\n")

        if not ask_yes_no("Would you like to order another item?"):
            break

    return order


def calculate_order(menu_dict, order_dict):
    subtotals = {}
    running_total = 0.00

    for item_name, quantity in order_dict.items():
        price = menu_dict[item_name]
        subtotal = price * quantity
        subtotals[item_name] = subtotal
        running_total += subtotal

    return subtotals, running_total

"""discount.py - decides which discount (if any) applies."""

from inputs import ask_yes_no


def apply_discount(total):
    discount_amount = 0.00
    discount_label = "None"

    is_senior_or_pwd = ask_yes_no("Are you a Senior Citizen or PWD?")

    if is_senior_or_pwd:
        discount_amount = total * 0.20
        discount_label = "Senior Citizen / PWD Discount (20%)"
    elif total >= 500:
        discount_amount = total * 0.10
        discount_label = "Loyalty Discount for orders >= PHP 500 (10%)"

    return discount_amount, discount_label

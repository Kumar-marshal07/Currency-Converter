"""
Currency Converter (console)
Concepts: Functions, Conditions, Operators, Dictionaries
Every conversion goes through INR. Results are rounded to 2 decimal places.
"""

import sys

# Exchange rates: value of 1 unit of the currency in INR
RATES_TO_INR = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105,
}


def validate_currency(code):
    """Return the cleaned currency code, or None if unsupported."""
    code = code.strip().upper()
    if code in RATES_TO_INR:
        return code
    return None


def validate_amount(text):
    """Return (amount, error_message). error_message is None if valid."""
    try:
        amount = float(text)
    except ValueError:
        return None, "Invalid amount. Enter a number."
    if amount != amount or amount in (float("inf"), float("-inf")):
        return None, "Invalid amount. Enter a number."
    if amount < 0:
        return None, "Amount cannot be negative."
    return amount, None


def convert_to_inr(amount, from_currency):
    """Convert an amount in from_currency to INR."""
    return amount * RATES_TO_INR[from_currency]


def convert_from_inr(amount_inr, to_currency):
    """Convert an amount in INR to to_currency."""
    return amount_inr / RATES_TO_INR[to_currency]


def convert_currency(amount, from_currency, to_currency):
    """Convert between any two supported currencies via INR (rounded to 2 dp)."""
    if from_currency == to_currency:
        return round(amount, 2)
    inr = convert_to_inr(amount, from_currency)
    return round(convert_from_inr(inr, to_currency), 2)


def fmt_amount(amount):
    """Show the input amount neatly: 166.0 -> 166, 12.5 -> 12.5"""
    return str(int(amount)) if amount == int(amount) else str(amount)


def run_conversion(amount_text, from_code, to_code):
    """Validate inputs, convert, and return the message to display."""
    from_currency = validate_currency(from_code)
    if from_currency is None:
        return "Unsupported currency '{}'. Available: {}".format(
            from_code.strip().upper(), ", ".join(RATES_TO_INR))

    to_currency = validate_currency(to_code)
    if to_currency is None:
        return "Unsupported currency '{}'. Available: {}".format(
            to_code.strip().upper(), ", ".join(RATES_TO_INR))

    amount, error = validate_amount(amount_text)
    if error:
        return error

    result = convert_currency(amount, from_currency, to_currency)
    return "{} {} = {:.2f} {}".format(
        fmt_amount(amount), from_currency, result, to_currency)


def run_tests():
    """Quick check against the given test cases."""
    cases = [
        (("166", "INR", "USD"), "166 INR = 2.00 USD"),
        (("0", "USD", "INR"), "0 USD = 0.00 INR"),
        (("100", "JPY", "USD"), "Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP"),
        (("abc", "USD", "INR"), "Invalid amount. Enter a number."),
        (("-50", "USD", "INR"), "Amount cannot be negative."),
        (("100", "USD", "EUR"), "100 USD = 92.22 EUR"),
        (("2", "GBP", "INR"), "2 GBP = 210.00 INR"),
        (("45", "EUR", "USD"), "45 EUR = 48.80 USD"),
    ]
    for args, expected in cases:
        got = run_conversion(*args)
        print("PASS" if got == expected else "FAIL", "|", got)


def main():
    print("=== Currency Converter ===")
    print("Supported currencies:", ", ".join(RATES_TO_INR))
    while True:
        amount_text = input("\nAmount: ")
        from_code = input("From: ")
        to_code = input("To: ")
        print(run_conversion(amount_text, from_code, to_code))
        again = input("\nConvert another? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()

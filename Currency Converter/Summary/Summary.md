# Currency Converter – Project Summary

## 1. Overview

This is a console-based Currency Converter written in Python. The user enters an amount, a source currency and a target currency, and the program displays the converted amount rounded to 2 decimal places. It supports four currencies: **INR, USD, EUR and GBP**.

## 2. Concepts Used

- **Functions:** the program is split into small, reusable functions such as `validate_currency()`, `validate_amount()`, `convert_currency()` and `run_conversion()`.
- **Conditions:** `if` statements check for unsupported currencies, invalid amounts and negative amounts.
- **Operators:** arithmetic operators (`*`, `/`) perform the conversion, and comparison operators validate the input.
- **Dictionaries:** the `RATES_TO_INR` dictionary stores the value of 1 unit of each currency in INR.

## 3. How It Works

1. Every conversion goes through INR: the amount is first converted to INR, then from INR to the target currency.
2. Currency codes are case-insensitive and extra spaces are ignored (`usd`, `USD` and ` Usd ` all work).
3. Input is validated in this order: source currency, target currency, then amount.
4. After each result, the user can choose `y` to convert again or `n` to exit.

**Exchange rates used (1 unit in INR):** INR = 1, USD = 83, EUR = 90, GBP = 105.

## 4. Input Validation

| Invalid input | Message shown |
|---|---|
| Unsupported currency (e.g. JPY) | Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP |
| Non-numeric amount (e.g. abc) | Invalid amount. Enter a number. |
| Negative amount (e.g. -50) | Amount cannot be negative. |

## 5. Test Cases and Results

| Test Case | Input | Output | Result |
|---|---|---|---|
| 1. Normal | 166, INR → USD | 166 INR = 2.00 USD | Pass |
| 2. Boundary | 0, USD → INR | 0 USD = 0.00 INR | Pass |
| 3a. Invalid currency | 100, JPY → USD | Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP | Pass |
| 3b. Invalid amount | abc, USD → INR | Invalid amount. Enter a number. | Pass |
| 3c. Negative amount | -50, USD → INR | Amount cannot be negative. | Pass |
| 4a. Valid scenario | 100, USD → EUR | 100 USD = 92.22 EUR | Pass |
| 4b. Valid scenario | 2, GBP → INR | 2 GBP = 210.00 INR | Pass |
| 4c. Valid scenario | 45, EUR → USD | 45 EUR = 48.80 USD | Pass |

All 8 test cases pass. They can also be run together with `python main.py test`.

## 6. Conclusion

The program converts between the supported currencies correctly, handles invalid input with clear error messages, and passes all the given test cases.
# Currency Converter

**Name:** MURARI MAHTO
**Class/Section:** M
**ERP:** RU-26-01688
**PS No.:** 32
**University:** Rungta International Skills University

---

## Project Description

This program is a console-based currency converter. Every conversion goes through INR, and results are rounded to 2 decimal places. It includes the following features:

- Converts between INR, USD, EUR and GBP
- Currency codes are case-insensitive (`usd`, `USD`, ` Usd ` all work)
- Invalid input (text, negative, `nan` or `inf` amount) shows an error message
- Unsupported currencies show the list of available currencies
- Option to convert again without restarting
- Built-in test mode with 8 test cases

## Libraries Required

- No external libraries are required.
- Only Python's built-in `sys` module is used.

Python 3.6 or higher is recommended.

## Steps to Run

1. Install Python (3.6 or higher).
2. Open the project code folder.
3. Run the following command in the Terminal/Command Prompt:

```bash
python main.py
```

To run the built-in test cases:

```bash
python main.py test
```

> **Note:** `main.py` must be in the folder where you run the command.

## Program Flow

1. Enter the Amount
2. Enter the currency to convert From
3. Enter the currency to convert To
4. See the result, then choose `y` to convert again or `n` to exit

## Exchange Rates (Value of 1 unit in INR)

```
INR : 1
USD : 83
EUR : 90
GBP : 105
```

## Sample Input

```
Amount: 100
From: usd
To: eur
Convert another? (y/n): n
```

## Sample Output

**Normal conversion**

```
=== Currency Converter ===
Supported currencies: INR, USD, EUR, GBP

100 USD = 92.22 EUR

Convert another? (y/n): n
Goodbye!
```

**More examples**

```
166 INR = 2.00 USD
0 USD = 0.00 INR
2 GBP = 210.00 INR
45 EUR = 48.80 USD
```

**Invalid inputs**

```
Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP
Invalid amount. Enter a number.
Amount cannot be negative.
```

**Test mode (`python main.py test`)**

```
PASS | 166 INR = 2.00 USD
PASS | 0 USD = 0.00 INR
PASS | Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP
PASS | Invalid amount. Enter a number.
PASS | Amount cannot be negative.
PASS | 100 USD = 92.22 EUR
PASS | 2 GBP = 210.00 INR
PASS | 45 EUR = 48.80 USD
```
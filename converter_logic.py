
EXCHANGE_RATES = {
    "USD": {"EUR": 0.92, "GBP": 0.79, "JPY": 156.76, "INR": 83.50, "AUD": 1.50, "CAD": 1.36, "USD": 1.0},
    "EUR": {"USD": 1.09, "GBP": 0.86, "JPY": 170.80, "INR": 91.00, "AUD": 1.63, "CAD": 1.48, "EUR": 1.0},
    "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 198.00, "INR": 105.50, "AUD": 1.90, "CAD": 1.72, "GBP": 1.0},
    "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "INR": 0.53, "AUD": 0.0096, "CAD": 0.0087, "JPY": 1.0},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095, "JPY": 1.89, "AUD": 0.018, "CAD": 0.016, "INR": 1.0},
    "AUD": {"USD": 0.67, "EUR": 0.61, "GBP": 0.53, "JPY": 104.50, "INR": 55.60, "CAD": 0.91, "AUD": 1.0},
    "CAD": {"USD": 0.74, "EUR": 0.68, "GBP": 0.58, "JPY": 115.20, "INR": 61.30, "AUD": 1.10, "CAD": 1.0}
}

def convert_currency(amount, source_currency, target_currency):
    source_currency = source_currency.upper()
    target_currency = target_currency.upper()

    if source_currency not in EXCHANGE_RATES:
        return None, f"Source currency \'{source_currency}\' not supported."
    if target_currency not in EXCHANGE_RATES[source_currency]:
        return None, f"Target currency \'{target_currency}\' not supported for conversion from \'{source_currency}\'."

    rate = EXCHANGE_RATES[source_currency][target_currency]
    converted_amount = amount * rate
    return converted_amount, None




EXCHANGE_RATES = {
    "USD": {"EUR": 0.92, "GBP": 0.79, "JPY": 156.76, "USD": 1.0},
    "EUR": {"USD": 1.09, "GBP": 0.86, "JPY": 170.80, "EUR": 1.0},
    "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 198.00, "GBP": 1.0},
    "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "JPY": 1.0}
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



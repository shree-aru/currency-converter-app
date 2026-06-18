import urllib.request
import json

def get_live_rates(base_currency="USD"):
    """Fetch live exchange rates from a public API."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        return data.get("rates", {})
    except Exception as e:
        print(f"Error fetching live rates: {e}")
        return None

def convert_with_live_api(amount, source_currency, target_currency):
    """Convert currency using live API rates."""
    source_currency = source_currency.upper()
    target_currency = target_currency.upper()

    rates = get_live_rates(source_currency)
    
    if not rates:
        return None, "Failed to retrieve live rates. Please check your internet connection."
    
    if target_currency not in rates:
        return None, f"Target currency '{target_currency}' is not supported by the live API."

    conversion_rate = rates[target_currency]
    converted_amount = amount * conversion_rate
    
    return converted_amount, None

if __name__ == "__main__":
    print("\n--- Live API Currency Converter ---")
    amount_str = input("Enter amount to convert: ")
    try:
        amount = float(amount_str)
        source = input("Enter source currency (e.g., USD): ")
        target = input("Enter target currency (e.g., EUR): ")
        
        print("\nFetching live rates... Please wait.")
        result, error = convert_with_live_api(amount, source, target)
        
        if error:
            print(f"Error: {error}")
        else:
            print(f"Success! {amount:.2f} {source.upper()} is exactly {result:.2f} {target.upper()} (Live Rate)")
            
    except ValueError:
        print("Invalid amount entered.")

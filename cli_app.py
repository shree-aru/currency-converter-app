
from converter_logic import convert_currency, EXCHANGE_RATES

def main():
    print("\n--- Currency Converter CLI ---")
    print("Supported Currencies: ", ", ".join(EXCHANGE_RATES.keys()))

    while True:
        try:
            amount_str = input("Enter amount to convert (or 'exit' to quit): ")
            if amount_str.lower() == 'exit':
                break
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue

            source_currency = input("Enter source currency (e.g., USD): ").upper()
            target_currency = input("Enter target currency (e.g., EUR): ").upper()

            converted_amount, error = convert_currency(amount, source_currency, target_currency)

            if error:
                print(f"Error: {error}")
            else:
                print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

        except ValueError:
            print("Invalid amount. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("--- Exiting Currency Converter ---")

if __name__ == "__main__":
    main()



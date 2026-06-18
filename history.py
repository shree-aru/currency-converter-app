import json
import os
from datetime import datetime

HISTORY_FILE = "conversion_history.json"

def load_history():
    """Load conversion history from JSON file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_conversion(amount, source, target, result, rate):
    """Save a single conversion record to history."""
    history = load_history()
    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "source_currency": source,
        "target_currency": target,
        "result": round(result, 2),
        "exchange_rate": rate
    }
    history.append(record)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
    return record

def display_history(limit=10):
    """Display the last N conversion records."""
    history = load_history()
    if not history:
        print("No conversion history found.")
        return

    recent = history[-limit:]
    print(f"\n--- Last {len(recent)} Conversion(s) ---")
    for i, record in enumerate(recent, 1):
        print(f"{i}. [{record['timestamp']}] "
              f"{record['amount']} {record['source_currency']} -> "
              f"{record['result']} {record['target_currency']} "
              f"(Rate: {record['exchange_rate']})")

def clear_history():
    """Clear all conversion history."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("Conversion history cleared.")
    else:
        print("No history to clear.")

if __name__ == "__main__":
    print("--- Conversion History Manager ---")
    print("1. View History")
    print("2. Clear History")
    choice = input("Choose an option: ")
    if choice == "1":
        display_history()
    elif choice == "2":
        clear_history()

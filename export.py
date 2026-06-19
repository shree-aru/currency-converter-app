import csv
import os
from history import load_history
from datetime import datetime

def export_to_csv():
    """Export conversion history to a CSV file."""
    history = load_history()
    if not history:
        print("No history available to export.")
        return False
        
    export_dir = "exports"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        
    filename = os.path.join(export_dir, f"conversion_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(['Timestamp', 'Amount', 'Source Currency', 'Target Currency', 'Result', 'Exchange Rate'])
        
        # Write data
        for record in history:
            writer.writerow([
                record.get('timestamp', ''),
                record.get('amount', 0),
                record.get('source_currency', ''),
                record.get('target_currency', ''),
                record.get('result', 0),
                record.get('exchange_rate', 0)
            ])
            
    print(f"Successfully exported {len(history)} records to {filename}")
    return True

if __name__ == "__main__":
    export_to_csv()

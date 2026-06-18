import tkinter as tk
from tkinter import messagebox, ttk
from converter_logic import convert_currency, EXCHANGE_RATES

class CurrencyConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        self.root.configure(padx=20, pady=20)

        # Style
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 11, "bold"))

        # Amount
        ttk.Label(root, text="Amount:").grid(row=0, column=0, sticky="w", pady=10)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(root, textvariable=self.amount_var, font=("Helvetica", 12))
        self.amount_entry.grid(row=0, column=1, pady=10)

        # Currencies
        currencies = list(EXCHANGE_RATES.keys())
        
        ttk.Label(root, text="From:").grid(row=1, column=0, sticky="w", pady=10)
        self.from_var = tk.StringVar(value="USD")
        self.from_dropdown = ttk.Combobox(root, textvariable=self.from_var, values=currencies, state="readonly", width=18)
        self.from_dropdown.grid(row=1, column=1, pady=10)

        ttk.Label(root, text="To:").grid(row=2, column=0, sticky="w", pady=10)
        self.to_var = tk.StringVar(value="EUR")
        self.to_dropdown = ttk.Combobox(root, textvariable=self.to_var, values=currencies, state="readonly", width=18)
        self.to_dropdown.grid(row=2, column=1, pady=10)

        # Convert Button
        self.convert_btn = ttk.Button(root, text="Convert", command=self.perform_conversion)
        self.convert_btn.grid(row=3, column=0, columnspan=2, pady=20)

        # Result Label
        self.result_label = ttk.Label(root, text="Result: --", font=("Helvetica", 14, "bold"), foreground="blue")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def perform_conversion(self):
        try:
            amount = float(self.amount_var.get())
            if amount < 0:
                messagebox.showerror("Error", "Amount cannot be negative.")
                return

            source = self.from_var.get()
            target = self.to_var.get()

            converted_amount, error = convert_currency(amount, source, target)
            
            if error:
                messagebox.showerror("Conversion Error", error)
            else:
                self.result_label.config(text=f"Result: {converted_amount:.2f} {target}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterGUI(root)
    root.mainloop()

import time
import tkinter as tk
from tkinter import messagebox

class BankApplication:
    def __init__(self):
        self.password = 1234
        self.chances = 3
        self.balance = 1000
        self.transaction_history = []
        
        self.root = tk.Tk()
        self.root.title("Bank Application")

        self.pin_frame = tk.Frame(self.root)
        self.pin_frame.pack()

        self.pin_label = tk.Label(self.pin_frame, text="Enter Your Four Digit Pin :")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self.pin_frame)
        self.pin_entry.pack()

        self.pin_button = tk.Button(self.pin_frame, text="Submit", command=self.check_pin)
        self.pin_button.pack()

        print("WELCOME TO THE BANK")
        print("Please Insert Your Card ")

    def check_pin(self):
        entered_pin = int(self.pin_entry.get())
        if entered_pin != self.password:
            self.chances -= 1
            messagebox.showerror("Error", f"Wrong Pin Number\nYou Have {self.chances} chances left")
            if self.chances == 0:
                self.root.quit()
        else:
            self.main_menu()

    def main_menu(self):
        self.pin_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.balance_label = tk.Label(self.main_frame, text=f"Your Current Balance is: {self.balance}")
        self.balance_label.pack()

        options = [
            "BALANCE",
            "WITHDRAW BALANCE",
            "DEPOSIT BALANCE",
            "TRANSFER FUNDS",
            "TRANSACTION HISTORY",
            "EXIT"
        ]

        self.option_var = tk.StringVar()
        self.option_var.set(options[0])
        option_menu = tk.OptionMenu(self.main_frame, self.option_var, *options)
        option_menu.pack()

        self.withdraw_label = tk.Label(self.main_frame, text="Enter Withdraw Amount:")
        self.withdraw_label.pack()
        self.withdraw_entry = tk.Entry(self.main_frame)
        self.withdraw_entry.pack()

        self.deposit_label = tk.Label(self.main_frame, text="Enter Deposit Amount:")
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(self.main_frame)
        self.deposit_entry.pack()

        confirm_button = tk.Button(self.main_frame, text="Confirm", command=self.option_select)
        confirm_button.pack()

    def option_select(self):
        selected_option = self.option_var.get()
        if selected_option == "BALANCE":
            self.balance_label.config(text=f"Your Current Balance is: {self.balance}")
        elif selected_option == "WITHDRAW BALANCE":
            withdraw_amount = int(self.withdraw_entry.get())
            if self.balance < withdraw_amount:
                messagebox.showerror("Error", "Insufficient Balance")
            else:
                self.balance -= withdraw_amount
                self.transaction_history.append({"type": "Withdraw", "amount": withdraw_amount, "date_time": time.strftime("%Y-%m-%d %H:%M:%S")})
                self.balance_label.config(text=f"Your Current Balance is: {self.balance}")
        elif selected_option == "DEPOSIT BALANCE":
            deposit_amount = int(self.deposit_entry.get())
            self.balance += deposit_amount
            self.transaction_history.append({"type": "Deposit", "amount": deposit_amount, "date_time": time.strftime("%Y-%m-%d %H:%M:%S")})
            self.balance_label.config(text=f"Your Current Balance is: {self.balance}")
        elif selected_option == "TRANSFER FUNDS":
            # Implement the transfer functionality here.
            pass
        elif selected_option == "TRANSACTION HISTORY":
            self.transaction_history_window()
        elif selected_option == "EXIT":
            self.root.quit()

    def transaction_history_window(self):
        self.main_frame.destroy()
        history_frame = tk.Frame(self.root)
        history_frame.pack()

        history_label = tk.Label(history_frame, text="Transaction History:")
        history_label.pack()

        for transaction in self.transaction_history:
            transaction_info = f"Type: {transaction['type']}, Amount: {transaction['amount']}, Date and Time: {transaction['date_time']}"
            transaction_label = tk.Label(history_frame, text=transaction_info)
            transaction_label.pack()

        back_button = tk.Button(history_frame, text="Back to Main Menu", command=self.main_menu)
        back_button.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BankApplication()
    app.run()

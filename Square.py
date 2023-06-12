from tkinter import Tk, Label, Entry, Button, messagebox
from savings_account import SavingsAccount
from current_account import CurrentAccount


def create_savings_account():
    account_name = name_entry.get()
    account_number = int(number_entry.get())
    savings_account = SavingsAccount(account_name, account_number)
    operate_savings_account(savings_account)


def create_current_account():
    account_name = name_entry.get()
    account_number = int(number_entry.get())
    current_account = CurrentAccount(account_name, account_number)
    operate_current_account(current_account)


def operate_savings_account(account):
    def check_balance():
        messagebox.showinfo("Account Balance", f"Account Balance: {account.check_balance()}")

    def deposit():
        amount = float(amount_entry.get())
        messagebox.showinfo("Deposit", account.deposit(amount))

    def withdraw():
        amount = float(amount_entry.get())
        messagebox.showinfo("Withdraw", account.withdraw(amount))

    savings_window = Tk()
    savings_window.title("Savings Account")

    check_balance_btn = Button(savings_window, text="Check Balance", command=check_balance)
    check_balance_btn.pack()

    amount_label = Label(savings_window, text="Amount:")
    amount_label.pack()

    amount_entry = Entry(savings_window)
    amount_entry.pack()

    deposit_btn = Button(savings_window, text="Deposit", command=deposit)
    deposit_btn.pack()

    withdraw_btn = Button(savings_window, text="Withdraw", command=withdraw)
    withdraw_btn.pack()

    savings_window.mainloop()


def operate_current_account(account):
    def check_balance():
        messagebox.showinfo("Account Balance", f"Account Balance: {account.check_balance()}")

    def deposit():
        amount = float(amount_entry.get())
        messagebox.showinfo("Deposit", account.deposit(amount))

    def withdraw():
        amount = float(amount_entry.get())
        messagebox.showinfo("Withdraw", account.withdraw(amount))

    current_window = Tk()
    current_window.title("Current Account")

    check_balance_btn = Button(current_window, text="Check Balance", command=check_balance)
    check_balance_btn.pack()

    amount_label = Label(current_window, text="Amount:")
    amount_label.pack()

    amount_entry = Entry(current_window)
    amount_entry.pack()

    deposit_btn = Button(current_window, text="Deposit", command=deposit)
    deposit_btn.pack()

    withdraw_btn = Button(current_window, text="Withdraw", command=withdraw)
    withdraw_btn.pack()

    current_window.mainloop()


main_window = Tk()
main_window.title("Square View")

name_label = Label(main_window, text="Account Name:")
name_label.pack()

name_entry = Entry(main_window)
name_entry.pack()

number_label = Label(main_window, text="Account Number:")
number_label.pack()

number_entry = Entry(main_window)
number_entry.pack()

account_type_label = Label(main_window, text="Select Account Type:")
account_type_label.pack()

savings_btn = Button(main_window, text="Savings Account", command=create_savings_account)
savings_btn.pack()

current_btn = Button(main_window, text="Current Account", command=create_current_account)
current_btn.pack()

main_window.mainloop()

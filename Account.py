class Account:
    def __init__(self, account_name, account_number):
        self.accountName = account_name
        self.accountBalance = 2000000
        self.accountNumber = account_number

    def check_balance(self):
        return self.accountBalance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        else:
            self.accountBalance += amount
            return f"Deposit successful. New balance: {self.accountBalance}"

    def withdraw(self, amount):
        if amount > self.accountBalance:
            return "Insufficient funds"
        elif amount <= 0:
            return "Invalid amount"
        else:
            self.accountBalance -= amount
            return f"Withdrawal successful. New balance: {self.accountBalance}"

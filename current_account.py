from Account import Account

class CurrentAccount(Account):
    def __init__(self, account_name, account_number):
        super().__init__(account_name, account_number)

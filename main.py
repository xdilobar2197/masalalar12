# masalalar12

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        if self.balance == 0:
            return "Hisob bo'sh"
        else:
            return f"Balans: {self.balance}$"


account = BankAccount(0)
print(account.check_balance())


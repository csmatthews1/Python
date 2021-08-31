class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(BankAccount.can_withdraw(self.balance, amount)):
            self.balance -= amount
        else:
            print("insufficient funds: Charging a $5 fee.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance-amount > 0):
            return True
        else:
            return False
    
    @classmethod
    def print_all_balances(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")


account1 = BankAccount(0.02)
account2 = BankAccount(0.01, 1000)

account1.deposit(500).deposit(300).deposit(60).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(250).withdraw(50).withdraw(300).withdraw(100).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_balances();


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

class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.accounts = []
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
    def new_account(self,int_rate, balance):
        self.accounts.append(BankAccount(int_rate, balance))
    def make_deposit(self, amount, accountIndex=0):
        self.accounts[accountIndex].deposit(amount)
    def make_withdrawal(self, amount, accountIndex=0):
        self.accounts.withdraw(amount)
    def display_user_balance(self):
        print(f"User: {self.name}")
        for account in self.accounts:
            account.display_account_info()
    def transfer_money(self, other_user, amount, accountIndex=0):
        self.accounts[accountIndex].withdraw(amount)
        other_user.accounts[0].deposit(amount)

bob = User("Bob Jones", "bobby@gmail.com")
larry = User("Larry King", "larry@gmail.com")
bob.make_deposit(1000)
bob.new_account(0.04, 500)

bob.transfer_money(larry, 200, 1)
bob.display_user_balance()
larry.display_user_balance()
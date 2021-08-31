class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self;
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self;
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self;
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self;

jerry = User("Jerry Van Dyke", "jerry@comedy.com")
dick = User("Dick Van Dyke", "dick@comedy.com")
monty = User("Monty Python", "monty@python.com")

jerry.make_deposit(500).make_deposit(200).make_deposit(50).make_withdrawal(60).display_user_balance()
dick.make_deposit(300).make_deposit(600).make_withdrawal(60).make_withdrawal(200).display_user_balance();
monty.make_deposit(1000).make_withdrawal(350).make_withdrawal(75).make_withdrawal(150).display_user_balance()
jerry.transfer_money(monty, 100).display_user_balance()
monty.display_user_balance()

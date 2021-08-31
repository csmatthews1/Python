class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

jerry = User("Jerry Van Dyke", "jerry@comedy.com")
dick = User("Dick Van Dyke", "dick@comedy.com")
monty = User("Monty Python", "monty@python.com")

jerry.make_deposit(500)
jerry.make_deposit(200)
jerry.make_deposit(50)
jerry.make_withdrawal(60)
jerry.display_user_balance()

dick.make_deposit(300)
dick.make_deposit(600)
dick.make_withdrawal(60)
dick.make_withdrawal(200)
dick.display_user_balance();

monty.make_deposit(1000)
monty.make_withdrawal(350)
monty.make_withdrawal(75)
monty.make_withdrawal(150)
monty.display_user_balance()

jerry.transfer_money(monty, 100)
jerry.display_user_balance()
monty.display_user_balance()

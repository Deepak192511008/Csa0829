class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance")


atm = ATM(10000)
atm.check_balance()
atm.deposit(3000)
atm.withdraw(5000)
atm.check_balance()

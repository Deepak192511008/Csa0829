class Bank:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account No:", self.accno)
        print("Name:", self.name)
        print("Balance:", self.balance)


b = Bank(12345, "Amit", 5000)
b.deposit(2000)
b.withdraw(1000)
b.display()

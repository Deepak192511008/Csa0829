class Payroll:
    def __init__(self):
        self.name = ""
        self.empid = 0
        self.basic = 0

    def input(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Name: ")
        self.basic = float(input("Enter Basic Salary: "))

    def calculate(self):
        self.hra = self.basic * 0.20
        self.da = self.basic * 0.10
        self.net = self.basic + self.hra + self.da

    def slip(self):
        print("\n--- Salary Slip ---")
        print("ID:", self.empid)
        print("Name:", self.name)
        print("Basic:", self.basic)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("Net Salary:", self.net)


p = Payroll()

while True:
    print("\n1.Enter Details")
    print("2.Calculate Salary")
    print("3.Display Salary Slip")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        p.input()
    elif ch == 2:
        p.calculate()
        print("Salary Calculated")
    elif ch == 3:
        p.slip()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")

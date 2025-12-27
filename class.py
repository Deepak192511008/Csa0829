class rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("area =", self.l * self.b)

    def peri(self):
        print("perimeter =", 2 * (self.l + self.b))


class lap:
    def __init__(self, ram, rom, pro, store):
        self.ram = ram
        self.rom = rom
        self.pro = pro
        self.store = store

    def disp(self):
        print("config:")
        print("ram =", self.ram)
        print("rom =", self.rom)
        print("processor =", self.pro)
        print("storage =", self.store)


class lb:
    def __init__(self, i, n, a):
        self.i = i
        self.n = n
        self.a = a

    def display(self):
        print(self.i, self.n, self.a)


class inven:
    def __init__(self):
        self.l = []

    def ad(self, s, q):
        self.l.append([s, q])
        print("added")

    def remove(self, rs):
        for i in self.l:
            if i[0] == rs:
                self.l.remove(i)
                break

    def dis(self):
        print(self.l)


class att:
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def dis(self):
        print("attendance % =", (self.a / self.t) * 100)


class Emp:
    def __init__(self, l):
        self.l = l
        self.s = 0

    def cal(self):
        for i in self.l:
            self.s += i[1]

    def dis(self):
        print("total salary =", self.s)


# -------- MENU DRIVEN PROGRAM --------

inv = inven()

while True:
    print("\nMENU")
    print("1. Rectangle")
    print("2. Laptop")
    print("3. Library Book")
    print("4. Inventory")
    print("5. Attendance")
    print("6. Employee Salary")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        l = int(input("Enter length: "))
        b = int(input("Enter breadth: "))
        r = rect(l, b)
        r.area()
        r.peri()

    elif ch == 2:
        ram = input("Enter RAM: ")
        rom = input("Enter ROM: ")
        pro = input("Enter Processor: ")
        store = input("Enter Storage: ")
        l = lap(ram, rom, pro, store)
        l.disp()

    elif ch == 3:
        i = int(input("Enter id: "))
        n = input("Enter name: ")
        a = input("Enter author: ")
        b = lb(i, n, a)
        b.display()

    elif ch == 4:
        print("1. Add item")
        print("2. Remove item")
        print("3. Display inventory")
        c = int(input("Enter choice: "))

        if c == 1:
            s = input("Enter item name: ")
            q = int(input("Enter quantity: "))
            inv.ad(s, q)
        elif c == 2:
            rs = input("Enter item name to remove: ")
            inv.remove(rs)
        elif c == 3:
            inv.dis()

    elif ch == 5:
        a = int(input("Enter attended classes: "))
        t = int(input("Enter total classes: "))
        c = att(a, t)
        c.dis()

    elif ch == 6:
        e = Emp([['e1', 156], ['e2', 453]])
        e.cal()
        e.dis()

    elif ch == 7:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class pro:

    class rect:
        def __init__(self, l, b):
            self.l = l
            self.b = b

        def area(self):
            self.t = self.l * self.b
            print("area =", self.t)

        def peri(self):
            print("perimeter =", 2 * (self.l + self.b))


    class lap:
        def __init__(self, ram, rom, pro, store):
            self.ram = ram
            self.rom = rom
            self.pro = pro
            self.store = store

        def disp(self):
            print("config=")
            print("ram =", self.ram)
            print("rom =", self.rom)
            print("processor =", self.pro)
            print("storage =", self.store)


    class lb:
        def __init__(self, i, n, a):
            self.i = i
            self.n = n
            self.a = a

        def display(self):
            print(self.i, self.n, self.a)


    class inven:
        def __init__(self):
            self.l = []

        def ad(self, s, q):
            self.l.append([s, q])
            print("added")

        def remove(self, rs):
            for i in self.l:
                if i[0] == rs:
                    self.l.remove(i)
                    break

        def dis(self):
            print(self.l)


    class att:
        def __init__(self, a, t):
            self.a = a
            self.t = t

        def dis(self):
            print("attendance % =", (self.a / self.t) * 100)


    class Emp:
        def __init__(self, l):
            self.l = l
            self.s = 0

        def cal(self):
            for i in self.l:
                self.s = self.s + i[1]

        def dis(self):
            print(self.s)


# ----- object creation -----

r = pro.rect(10, 5)
r.area()
r.peri()

l = pro.lap('16gb', '528gb', 'i5', 12324)
l.disp()

lb1 = pro.lb(1, 'emad', 'thr')
lb1.display()

i = pro.inven()
i.ad('pen', 10)
i.ad('e', 30)
i.ad('r', 45)
i.dis()
i.remove('e')
i.dis()

c = pro.att(65, 77)
c.dis()

e = pro.Emp([['e1', 156], ['e2', 453]])
e.cal()
e.dis()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class rect():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.t=self.l*self.b
        print("area=",self.t)
        
    def peri(self):
        print("perimeter=",2*(self.l+self.b))
r=rect(10,5)
r.area()
r.peri()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class lap():
    def __init__(self,ram,rom,pro,store):
        self.ram=ram
        self.rom=rom
        self.pro=pro
        self.store=store
    def disp(self):
        print("config=\nram=",self.ram,"rom=",self.rom,"processor=",self.pro,"storage=",self.store)
l=lap('16gb','528gb','i5',12324)
l.disp()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class lb():
    def __init__(self,i,n,a):
        self.i=i
        self.n=n
        self.a=a
    def display(self):
        print(self.i,self.n,self.a)
l=lb(1,'emad','thr')
l.display()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class inven():
    def __init__(self):
        self.l=[]
    def ad(self,s,q):
        self.l.append([s,q])
        print('added')
    def remove(self,rs):
        for i in self.l:
            if i[0]==rs:
                self.l.remove(i)
                break
    def dis(self):
        print(self.l)
i=inven()
i.ad('pen',10)
i.ad('e',30)
i.ad('r',45)
i.dis()
i.remove('e')
i.dis()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class att():
    def __init__(self,a,t):
        self.a=a
        self.t=t
    def dis(self):
        print("attendence %=",(self.a/self.t)*100)
c=att(65,77)
c.dis()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Emp:
    def __init__(self, l):
        self.l = l
        self.s = 0
    def cal(self):
        for i in self.l:
            self.s = self.s + i[1]
    def dis(self):
        print(self.s)
e = Emp([['e1', 156], ['e2', 453]])
e.cal()
e.dis()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class S:
    def __init__(self, n, m1, m2, m3):
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.t = self.m1 + self.m2 + self.m3

    def d(self):
        print("Name:", self.n)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total:", self.t)


n = "Vijay"
m1 = 499
m2 = 451
m3 = 500

o = S(n, m1, m2, m3)
o.d()

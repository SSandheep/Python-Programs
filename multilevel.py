class addition:
    def gets(self):
        self.a = int(input("Enter a Number: "))
        self.b = int(input("Enter a Number: "))
    def calladd(self):
        self.c = self.a+self.b
    def disadd(self):
        print("Add: ", self.c)


class subtraction(addition):
    def callsub(self):
       self.d = self.a-self.b
    def dissub(self):
        print("Sub: ", self.d)


class multiplication(subtraction):
    def callmul(self):
        self.e = self.a*self.b
    def dismul(self):
        print("Mul: ", self.e)


a1 = multiplication()
a1.gets()
a1.calladd()
a1.disadd()
a1.callsub()
a1.dissub()
a1.callmul()
a1.dismul()

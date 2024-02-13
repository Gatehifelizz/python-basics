class Fruits:

    def __init__(self,name,price):
        self.name = name
        self.price =price

    def fruity(self):
        print(f"I bought a {self.name} for {self.price}")
obj1 = Fruits("mango","ksh 30")
obj1.fruity()
obj2 = Fruits("banana","ksh 25")
obj2.fruity()
obj3 = Fruits("peach","ksh 50")
obj3.fruity()
obj4 = Fruits("pear","ksh 25")
obj4.fruity()
obj5 = Fruits("coconut","ksh 70")
obj5.fruity()

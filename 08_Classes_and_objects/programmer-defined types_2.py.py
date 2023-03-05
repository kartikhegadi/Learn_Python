class Person:

    def __init__(self, na, ge, ag):
        self.name = na
        self.gender = ge
        self.age = ag

    def talk(self):
        print("hi my name is ", self.name)

    def vote(self):
        if self.age >= 18:
            print("You can vote")
        else:
            print("print you can't vote")


obj1 = Person('kartii', 'male', 22)
obj1.talk()


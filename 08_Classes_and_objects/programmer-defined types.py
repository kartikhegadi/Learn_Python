class Person:

    def __init__(self):
        self.name = "kartik"
        self.gender = 'male'
        self.age = 21

    def talk(self):
        print("hi my name is ",self.name)

    def vote(self):
        if self.age >= 18:
            print("You can vote")
        else:
            print("print you can't vote")

obj  = Person()
obj.talk()
obj.vote()
Person.talk(obj)
Person.vote(obj)

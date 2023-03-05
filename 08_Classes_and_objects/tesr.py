class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def talk(self):
        print("hi i am", self.name)

    def vote(self):
        if self.age < 18:
            print("i am not eligible \n")
        else:
            print("I am eligible to vote \n")


obj1 = person('pattern', 'male', 18)
obj2= person('kartik', 'male', 18)

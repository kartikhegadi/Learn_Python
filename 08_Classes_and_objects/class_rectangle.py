class rectangle:

    def __init__(self):
        self.width = 10;
        self.bredth = 20;

    def rectangl_cof(self):
        print("The ractangle conf is", self.width, self.bredth)

    def fnd_center(self):
        print("the center is", ((self.width + self.bredth) / 2))


rect = rectangle()
rect.rectangl_cof()
rect.fnd_center()

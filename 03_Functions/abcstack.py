def a():
    print('a() start')
    b()
    d()
    print("returned from d ")
def b():
    print("b() start")
    c()
def c():
    print("c() starts")
def d():
    print("d starts")

# starting a
a()

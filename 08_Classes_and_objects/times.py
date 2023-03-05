class time:
    """represens the time of day
        attributes : hour : minut: second """

    def __init__(self, hour=0, minut=0, second=0):
        self.hour = hour
        self.minut = minut
        self.second = second

    def timess(self):
        print("The time HOUR:MINUT:SECOND", self.hour, self.minut, self.second)


def time_adder(t1, t2):
    sum = time()
    sum.hour = t1.hour + t2.hour
    sum.minut = t1.minut + t2.minut
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second=sum.second-60
        sum.minut=+1
    if sum.minut >= 60:
        sum.minut=sum.second-60
        sum.hour=sum.hour+1
    print("the total sum of the time is ", sum.hour, sum.minut, sum.second)



k1=time(12,60,60)
k2=time(44,70,30)
time_adder(k1,k2)




import random
def get_ans(key):
    if key == 1:
        return ' its 1'
    elif key == 2:
        return 'its 2'
    elif key ==5:
        return ' its 5'
    elif key == 6:
        return 'its 6'

for i in range(10):
    r = random.randint(1,5)
    fortune=get_ans(r)
    print(fortune)
import operator
import random

ops = {'+': operator.add,
       '-': operator.sub}  # add mul and div if you wish

keys_tuple = tuple(ops.keys())
num_a = random.randint(1, 10)  # use larger range if you wish
num_b = random.randint(1, 10)  # use larger range if you wish
op = random.choice(keys_tuple)

print('{}{}{}=?'.format(num_a, op, num_b))
expected_answer = ops[op](num_a, num_b)
user_answer = int(input())
if user_answer == expected_answer:
    print('Correct')
else:
    print('Wrong')
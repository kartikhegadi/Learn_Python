def spam():
    print(eggs)    # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)
# prints 'bacon local'
# prints 'bacon local'




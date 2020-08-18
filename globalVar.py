a = 10
print(id(a))

def something():
    a =15
    x  = globals()['a']
    print(id(x))
    print("in fun", a)

something()
print("outside ", a)
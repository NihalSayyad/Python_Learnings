def fib(n):
    a = 0
    b = 1
    if (n >2):
        print(a)
        print(b)
    elif (n>0):
        print(a)
    else:
        print("Not a valid number")
    c = a + b

    while(c<n):
        a = b
        b = c
        print(c)
        c = a + b


fib(2)
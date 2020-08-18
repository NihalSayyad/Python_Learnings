def fib(n):
    a = 0
    b = 1

    print(a)
    c = a + b

    while(c<n):
        a = b
        b = c
        print(c)
        c = a + b


fib(10)
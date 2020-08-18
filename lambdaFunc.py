from functools import reduce

def square(a):
    return a*a

result = square(5)
print(result)

f = lambda a : a*a

result = f(4)
print(result)

def is_even(a):
    return a%2 == 0

lst = [2,3,4,5,3,4,5,6,34,56,55,57,6,8,9,12,13]

evens = list(filter(lambda n: n%2==0,lst))
doubles = list(map(lambda a:a*2,evens))
sum = reduce(lambda a,b : a+b,doubles)
print(evens)
print(doubles)
print(sum)
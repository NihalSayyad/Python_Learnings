
def bs(a):
    num = len(a)-1

    for i in range(num):
        for j in range(num-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

lst = [6,7,45,2,5,78,12,3,7]

bs(lst)
print(lst)
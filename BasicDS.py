
from array import *

arr = array('i',[1,2,3,4,5])

#accessing array elements using index
print(arr[0])
print(arr[3])

#insert operation
arr.insert(16,10)

for i in arr:
    print(i)

print(arr.index(10))

# LIST #
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]

l3 = l1 + l2
print(l3)
del l1
del l2[1]
l3.append(34)
print(l3.index(5))

# TUPLE #
tup1 = (1,2,3,4)
tup2 = (3,4,5,6)

tup3 = tup1 + tup2
print(tup3 * 4)

# DICT #
listofInts = [7, 10, 45, 23, 77]
listofStrings = ["Hello", "hi", "there", "at", "this"]

a = zip(listofStrings,listofInts)
print(next(a))

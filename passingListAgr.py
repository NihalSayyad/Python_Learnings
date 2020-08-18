
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = [10,23,24,55,47,30,389,45,22,26]
even, odd = count(lst)

print(f"Even : {even} \nOdd: {odd}")
'''

def persom(name,age=18):
    print(name)
    print(age)

#positional arg
persom('nihal', 26)

#keyword
persom(age=26, name='Mukesh')

#defaul
persom('Nihal')

#variable length
def sum(*b):
    c = 0
    for i in b:
        c = c+i
    print(c)

sum(5,6,7,8)
'''

def person_data(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

        

person_data('Nihal', age=26, city='Pune', mob=987654321)





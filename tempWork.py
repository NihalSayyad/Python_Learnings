def unique_ele(a):
    unique_lst=[]
    for i in a:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

def duplicate_ele(a):
    duplicate_lst=[]
    for i in range(len(a)):
        if a[i] in a[i+1:len(a)-1]:
            if a[i] not in duplicate_lst:
                duplicate_lst.append(a[i])
    return duplicate_lst

def reverse_string(a):
    ret_str = ""
    lst = a.split()
    for i in lst:
        i = i[::-1]
        ret_str= ret_str+" "+i
        print(id(ret_str))
    return ret_str

def palindrome(a):
    for i in range(int(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return False
    return True

def temp1(a):
    a = 5

a=10
print(a)
temp1(a)
print(a)

a = "palindromemordnila"
print(f"status palindrome : {palindrome(a)}" )

string = "hi this is new string"
print(reverse_string(string))

#lst = [1,2,3,4,5,2,3,1,2,7,4,5,6,8,5]
#lst = duplicate_ele(lst)
#print(lst)


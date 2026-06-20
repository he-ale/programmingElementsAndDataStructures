
def exercise18(n: int, flag: bool= True, a: int= 0, b: int= 0):
    if (n==0):
        return a-b if flag else b-a

    aux= n%10
    if flag:
        a+=aux
    else:
        b+=aux
    return exercise18(n//10, not flag, a, b)

def other(n: int):
    a= 0
    b= 0
    flag= True
    while n!=0:
        aux= n%10
        if flag:
            a+=aux
        else:
            b+=aux
        n//=10
        flag= not flag
    return a-b if flag else b-a

print(exercise18(318547))
print(other(318547))
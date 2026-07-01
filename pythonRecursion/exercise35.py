from typing import List

def convination(n, k):
    if (k==0 or k==n):
        return 1
    return ((n-k+1)/k)*convination(n, k-1)

def getLevel(n: int, xs: List[int], i: int):
    if(n<i):
        return xs
    a= convination(n, i)
    xs.append(str(int(a)))
    return getLevel(n, xs, i+1)

def exercise35(n: int):
    if n==0:
        return "1"
    if n==1:
        return "1 1"
    xs= []
    getLevel(n, xs, 0)    
    return " ".join(xs)

def other(n: int):
    xs= []
    i= 0
    while (i <= n):
        a= str(int(convination(n, i)))
        xs.append(a)
        i+=1
    return " ".join(xs)

print(other(0))
print(other(1))
print(other(2))
print(other(4))
print(other(5))

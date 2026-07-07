from typing import List
from math import sqrt

#########################################
# Recusive Solution
#########################################
def __prime__(n: int, i:int= 2):
    if (i>sqrt(n)):
        return True
    if (n%i==0):
        return False
    return __prime__(n, i+1)

def exercise44(n: int, xs: List[int]=[2,3], rs: List[int]= [2,3]):
    if n==1:
        return [2]
    if n==2:
        return [2, 3]
    if n==len(rs):
        return rs

    xs.append(xs[-1]+xs[-2])
    if __prime__(xs[-1]):
        rs.append(xs[-1])

    return exercise44(n, xs, rs)

#########################################
# Iterative Solution
#########################################
def __isPrime__(n: int):
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def other(n: int):
    if(n==1):
        return [2]
    if(n==2):
        return [2, 3]
    rs=[2,3]
    fibonacci=[2,3]
    while (len(rs)!=n):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
        if __isPrime__(fibonacci[-1]):
            rs.append(fibonacci[-1])
    return rs 

print(exercise44(5))
print(other(5))

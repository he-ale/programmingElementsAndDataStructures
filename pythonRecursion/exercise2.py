import math



def isPrimeNumber(n: int, i: int)->bool:
    if (i == 1):
        return True
    
    if ( n%i==0):
        return False
    
    return isPrimeNumber(n= n, i= i-1)

def exercise2(n: int)->bool:
    i= int(math.sqrt(n))
    return isPrimeNumber(n=n, i=i)

print(exercise2(37))
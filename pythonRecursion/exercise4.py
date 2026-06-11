from typing import List
import math

def findPrimeFactors(n: int, i:int=2, primeFactors: List[int]=[]):
    if( n==1 ):
        return primeFactors

    if( n%i==0 ):
        if ( len(primeFactors)==0 ):
            primeFactors.append(i)
        elif ( primeFactors[-1]!=i ):
            primeFactors.append(i)

        findPrimeFactors(n=n//i, i=i, primeFactors= primeFactors)
    else:
        findPrimeFactors(n, i=i+1, primeFactors= primeFactors)

def exercise4(n: int):
    factors=[]
    findPrimeFactors(n, i= 2, primeFactors= factors)
    return factors
    

def other(n: int)->List[int]:
    factors= []
    i= 2

    while n>1:
        if( n%i==0 ): 
            if (len(factors)==0):
                factors.append(i)
            elif (factors[-1]!=i):
                factors.append(i)      
            n=n//i
        else: 
            i= i+1

    return factors

print(exercise4(25))
print(other(20))

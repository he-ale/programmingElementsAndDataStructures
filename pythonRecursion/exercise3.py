

def exercise3(n: int)->int:
    if(n==0):
        return 0
    return 1 + exercise3(n//10)

def other(n: int )->int:
    digits= 0
    while( n!=0 ):
        n=n//10
        digits= digits+1
    
    return digits

print(exercise3(151))
print(other(151))
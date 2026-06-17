

def exercise14(n: int):
    if (n%2==1):
        return False
    
    if (n==0):
        return True
    
    return exercise14(n//10)

def other(n:int):
    res= True
    while(n>0 and res):
        res= (n%10)%2==0
        n= n//10
    return res

print(other(242))

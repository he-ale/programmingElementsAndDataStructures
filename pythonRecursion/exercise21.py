
def exercise21(n: int, total: int= 0):
    if(n==0):
        return total
    
    return exercise21(n-1, total+(4*n+2))

def other(n: int):
    total= 0
    while(n>0):
        total+= (4*n+2)
        n-=1
    return total

print(exercise21(3))
print(other(3))
#########################################
# Solution 1 (better)
#########################################
def exercise30(n: int, a: int=0, b: int=0, flag: bool= True):
    if n==0:
        return a if not flag else b
    
    aux= n%10

    if aux%2==0:
        if flag:
            a+=1
        else:
            b+=1
    
    return exercise30(n//10, a, b, not flag)

#########################################
# Solution 2 (worse)
#########################################

def recursive(ls, i):
    if i==len(ls):
        return 0
    
    if(i%2==0):
        if(int(ls[i])%2==0):
            return 1 + recursive(ls, i+1)
        
    
    return recursive(ls, i+1)


def exercise30v2(n: int):
    return recursive(list(str(n)), 0)

#########################################
# Iterative solution
#########################################

def other(n: int):
    flag= True
    counterA=0
    counterB=0
    while(n!=0):
        digit= n%10
        if( digit%2==0):
            if( flag ):
                counterA+=1
            else:
                counterB+=1
        n//=10
        flag= not flag
    
    return counterB if flag else counterA

print(exercise30(22005))
print(exercise30(201414))


print(other(22005))
print(other(201414))
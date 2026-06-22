
def isValid(n: int, digit: int):
    if (n%10>digit):
        return False
    if(n==0):
        return True
    return isValid(n//10, n%10)

def exercise23(n: int):
    if(n<10):
        return True
    return isValid(n//10, n%10)

def other(n: int):
    digit= n%10
    n//=10
    while(n>0):
        if(digit<n%10):
            return False
        digit= n%10
        n//=10
    return True

print(exercise23(1227))
print(exercise23(88))
print(exercise23(898))
print(other(1227))
print(other(88))
print(other(898))


def isValid(n: int, digit: int):
    if(n==0):
        return True
    if((digit-1)!=(n%10)):
        return False
    return isValid(n//10, n%10)

def exercise24(n: int):
    digit= n%10
    n//=10
    return isValid(n, digit)

def other(n:int):
    digit= n%10
    n//=10
    while(n>0):
        if((digit-1)!=(n%10)):
            return False
        digit=n%10
        n//=10
    return True

print(exercise24(1227))
print(exercise24(88))
print(exercise24(678))
print(other(1227))
print(other(88))
print(other(678))

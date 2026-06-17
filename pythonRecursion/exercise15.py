

def exercise15(n: int, digits: int= 0, a: int= 0, b: int=0, flag: bool= True):
    if(n==0):
        value= 0
        if(digits%2==0):
            value= b-a
        else:    
            value= a-b
        if(value==0 or value==11):
            return True
        elif(value<11):
            return False
        else:
            return exercise15(value, 0, 0, 0, True)
    
    if flag:
        a= a + (n%10)
    else:
        b= b + (n%10)

    digits=digits+1
    flag= not flag
    n= n//10
    return exercise15(n, digits, a, b, flag)


def other(n:int):
    return n%11==0

print(exercise15(165))


def exercise15(a: int, b: int ):
    if( a <= b ):
        return str(a)
    
    n1= a//b
    n2= a-n1
    if (n1<=b):
        if(n2<=b):
            return str(n1) + str(n2)
        else:
            return str(n1)+exercise15(n2,b)
    
    return exercise15(n1,b) + exercise15(n2,b)

print(exercise15(10, 3))

    

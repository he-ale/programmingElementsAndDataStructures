
def recursive(i: int):
    if(i==1):
        return "1"
    return str(i)+recursive(i-1)

def patern(n: int, i: int, result: str= ""):
    if(i==n):
        return result+ recursive(i)
    
    result+= recursive(i)
    return patern(n, i+1, result+"\n")
    
def exercise22(n: int):
    return patern(n, 1)

def other(n: int):
    aux= ""
    result= ""
    for i in range(1,n+1, 1):
        if(i==1):
            aux= str(i)+aux
            
        else:
            aux= str(i)+aux
        result= result+"\n"+aux if result!="" else aux
    return result

# print(exercise22(9))
print(other(8))

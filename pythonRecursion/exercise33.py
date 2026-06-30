#########################################
# Recursive solution 
#########################################

def getSecondOccurrences(n: str, i: int= 0, rs: str= ""):
    if(i==len(n)):
        return int(rs)
    if n[i] in rs:
        return getSecondOccurrences(n, i+1, rs)
    return getSecondOccurrences(n, i+1, f"{rs}{n[i]}")

def exercise33(n: int):
    return getSecondOccurrences(str(n))

#########################################
# Iterative solution 
#########################################
def other(n: int):
    num= str(n)
    rs= ''
    for e in num:
        if e not in rs:
            rs= f"{rs}{e}"
    return int(rs)

print(exercise33(2356342))
print(other(2356342))


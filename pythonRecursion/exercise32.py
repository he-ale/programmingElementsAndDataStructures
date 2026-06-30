#########################################
# Recursive solution 
#########################################

def exercise32(n: int, number: str=""):
    if (n==0):
        return int(number)
    
    num= n%10
    if str(num) not in number:
        number= f"{num}{number}"
    return exercise32(n//10, number)

#########################################
# Iterative solution 
#########################################

def other(n: int):
    number= ''
    while (n>0):
        num= n%10
        if str(num) not in number:
            number= f"{num}{number}"
        n//=10
    return int(number)


print(exercise32(2356342))
print(other(2356342))

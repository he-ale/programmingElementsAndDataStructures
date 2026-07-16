
#########################################
# Recusive Solution
#########################################
def exercise47(n: int):
    if (n == 1):
        return "(-.-)"
    
    return f"(-.{exercise47(n-1)}.-)"


#########################################
# Iterative Solution
#########################################
def other(n: int):
    if (n == 1):
        return "(-.-)"
    result= "(-.-)"
    while (n != 1):
        result= f"(-.{result}.-)"
        n-=1
    return result


print(exercise47(1))
print(exercise47(3))
print(other(1))
print(other(3))

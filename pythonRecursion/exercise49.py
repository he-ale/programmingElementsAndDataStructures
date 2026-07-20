dictionary= {"H": "‾", "L": "_"}
#########################################
# Recusive Solution
#########################################

def __recursive__(cad: str, i: int, current: str):
    if (len(cad) == i):
        return -1
    if (cad[i] == current ):
        return __recursive__(cad, i+1, current)
    
    return 1+__recursive__(cad, i+1, cad[i])
     
def exercise49(cad: str):
    if (len(cad) == 0):
        return 0
    return __recursive__(cad, 0, cad[0])

#########################################
# Iterative Solution
#########################################

def other(cad: str):
    resutlt= 0
    current= cad[0]
    cad= cad[1:] 
    for c in cad:
        if (c != current):
            resutlt+= 1
            current= c
        
    return resutlt-1

print(exercise49("HHHHLLLLHHHHHLLHHLLHHL"))
print(other("HHHHLLLLHHHHHLLHHLLHHL"))

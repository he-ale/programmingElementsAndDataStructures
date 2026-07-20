dictionary= {"H": "‾", "L": "_"}
#########################################
# Recusive Solution
#########################################

def __recursive__(cad: str, i: int, current: str):
    if (len(cad) == i):
        return ""
    if (cad[i] == current ):
        return f"{dictionary[current]}{__recursive__(cad, i+1, current)}"
    
    return f"|{dictionary[cad[i]]}{__recursive__(cad, i+1, cad[i])}"
     
def exercise50(cad: str):
    if (len(cad) == 0):
        return ""
    return __recursive__(cad, 0, cad[0])

#########################################
# Iterative Solution
#########################################

def other(cad: str):
    resutlt= dictionary.get(cad[0])
    current= cad[0]
    cad= cad[1:] 
    for c in cad:
        if (c == current):
            resutlt= f"{resutlt}{dictionary[c]}"
        else:
            resutlt= f"{resutlt}|{dictionary[c]}"
            current= c
    return resutlt

print(exercise50("HHHHLLLLHHHHHLLHHLLHH"))
print(other("HHHHLLLLHHHHHLLHHLLHH"))

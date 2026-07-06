def __generate__(current:str, counter:int):
    if counter%2==1:
        return current*(counter-1)
    else:
        return current*counter

#########################################
# Recursive Solution
#########################################

def __recursion__(word: str, current: str, counter, i: int):
    if (i==len(word)):
        return __generate__(current, counter)
    
    if(current!=word[i]):
        aux= __generate__(current, counter)
        return f"{aux}"+__recursion__(word, word[i], 1, i+1)
    
    return __recursion__(word, current, counter+1, i+1)

def exercise40(word: str):
    if len(word)==0:
        return ""
    return __recursion__(word, word[0], 1, 1)

#########################################
# Iterative Solution
#########################################
def other(word: str):
    if len(word)==0:
        return ""
    current= word[0]
    counter= 1
    result=""
    for i in range(1, len(word)):
        if(current==word[i]):
            counter+=1
        else:
            result= f"{result}{__generate__(current, counter)}"
            current= word[i]
            counter=1

    return f"{result}{__generate__(current, counter)}"

print(exercise40("aaabbabbaa"))
print(other("aaabbabbaa"))
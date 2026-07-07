#########################################
# Recusive Solution
#########################################
def __recursive__(word: str, a: str, i: int):
    if (i>len(word)-len(a)+1):
        return 0
    if(a==word[i:i+len(a)]):
        return 1 + __recursive__(word, a, i+1)
    return __recursive__(word, a, i+1)

def exercise42(word: str, a:str):
    return __recursive__(word, a, 0)

#########################################
# Iterative Solution
#########################################
def other(word:str, a:str):
    counter= 0
    for i in range(len(word)-len(a)+1):
        if(a==word[i:i+len(a)]):
            counter+=1
    return counter



print(exercise42("aaabbabbaaa", "abba"))
print(other("aaabbabbaaa", "abba"))


#########################################
# Recusive Solution
#########################################
def __isPossible__(word:str, a:str, i: int, j: int):
    if(j==len(a)):
        return (i, True)
    elif(word[i]==a[j]):
        return __isPossible__(word, a, i+1, j+1)
    elif( j>0 and word[i]==a[j-1]):
        return __isPossible__(word, a, i+1, j)
    else:
        return (-1, False)
    

def __recursive__(word: str, a: str, i: int):
    if(i>len(word)-len(a)+1):
        return 0
    (k, flag)= __isPossible__(word, a, i, 0)
    if flag:
        return 1+ __recursive__(word, a, k-1)
    return __recursive__(word, a, i+1)

def exercise43(word: str, a: str):
    return __recursive__(word, a, 0)


#########################################
# Iterative Solution
#########################################
def other(word: str, a:str):
    counter= 0
    i=0
    while i < (len(word)-len(a)+1):
        j= 0
        k= i
        while(j< len(a)):
            if(a[j]==word[k]):
                j+=1
                k+=1
            elif(j>0 and a[j-1]==word[k]):
                k+=1
            else:
                break
        if(j==len(a)):
            counter+=1
            i=k-1
        else:
            i+=1
    return counter

print(exercise43('aaabbabcabaaba', 'aba'))
print(other('aaabbabcaba', 'aba'))

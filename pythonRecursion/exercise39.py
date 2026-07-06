#########################################
# Recursive Solution
#########################################

def __recursive39__(word: str, counter: int, i: int):
    if(i==len(word)):
        return f"{word[i-1]}{counter}"
    
    if(word[i-1]==word[i]):
        return __recursive39__(word, counter+1, i+1)

    return f"{word[i-1]}{counter}"+ __recursive39__(word, 1, i+1)

def exercise39(word: str):
    if len(word)==0:
        return ""
    return __recursive39__(word, 1, 1)

#########################################
# Iterative Solution
#########################################
def other(word: str):
    if len(word)==0:
        return ""
    counter= 1
    current= word[0]
    result= ''
    for i in range(1, len(word)):
        if (current==word[i]):
            counter+=1
        else:
            result= f'{result}{current}{counter}'
            counter=1
            current=word[i]

    return f'{result}{current}{counter}'

print(exercise39('gggbbddeeewwasss'))
print(other('gggbbddeeewwasss'))
print(exercise39('ggg'))
print(other('ggg'))

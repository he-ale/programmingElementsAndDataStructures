
def countOccurrences(word: str, letter: str, i: int, counter: int):
    if(i==len(word)):
       return letter+str(counter)

    if(word[i]==letter):
        return countOccurrences(word, letter, i+1, counter+1)
    
    return letter+str(counter)+countOccurrences(word, word[i], i+1, 1)

def exercise26(word: str):
    letter= word[0]
    i= 1
    counter=1
    return countOccurrences(word, letter, i, counter)

def other(word: str):
    letter= word[0]
    counter= 1
    res= ''
    for i in range(1, len(word), 1):
        if(word[i]==letter):
            counter+=1
        else:
            res+=letter+str(counter)
            letter= word[i]
            counter= 1
    return res+letter+str(counter)

print(exercise26('aaabb'))
print(exercise26('aaabbc'))
print(other('aaaebb'))
print(other('aaaebbc'))
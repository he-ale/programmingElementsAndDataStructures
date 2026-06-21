
def isPalindrome(word: str, i: int, j: int):
    if( i>=j ):
        return True
    
    if(word[i]!=word[j]):
        return False
    return isPalindrome(word, i+1, j-1)

def exercise20(word: str):
    return isPalindrome(word, 0, len(word)-1)


def other(word:str):
    i= 0
    j= len(word)-1

    while(i<j):
        if( word[i] != word[j]):
            return False
        i+=1
        j-=1
    return True

print(exercise20("ababa"))
print(exercise20("abba"))
print(exercise20("abca"))
print(exercise20("abdca"))
print(other("ababa"))
print(other("abba"))
print(other("abca"))
print(other("abdca"))
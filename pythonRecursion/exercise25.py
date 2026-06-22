
def buildSequence(word: str, letter: str, i: int, sequence: str):
    if(i < 0):
        return sequence
    if(word[i]==letter):
        return buildSequence(word, letter, i-1, sequence)
    return buildSequence(word, word[i], i-1, sequence+word[i])

def exercise25(word: str):
    return buildSequence(word, word[len(word)-1], len(word)-2, word[len(word)-1])


def other(word: str):
    i= len(word)-1
    letter= word[i]
    i-=1
    sequence= letter
    while(i>=0):
        if(letter!=word[i]):
            sequence= sequence+word[i]
            letter= word[i]
        i-=1
    return sequence

print(exercise25('aaabccdddaaebb'))
print(other('aaabccdddaaebb'))

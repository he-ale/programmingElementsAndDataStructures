#########################################
# Recursive Solution
#########################################

def __recurtion__(word: str, current: str, i: int):
    if (i==len(word)):
        return current if word[i-2]!=word[i-1] else ""
    if (current!=word[i]):
        return f"{current}"+ __recurtion__(word, word[i], i+1)
    return __recurtion__(word, current, i+1)

def exercise41(word: str):
    if len(word)==0:
        return ""
    return __recurtion__(word, word[0], 1)

#########################################
# Iterative Solution
#########################################
def other(word: str):
    if len(word)==0:
        return ""
    current= word[0]
    result= ""
    for i in range(1, len(word)):
        if (current!=word[i]):
            result= f"{result}{current}"
            current= word[i]
    return result if current==result[-1] else f"{result}{current}"

print(exercise41("aaabbaabba"))
print(other("aaabbaabba"))

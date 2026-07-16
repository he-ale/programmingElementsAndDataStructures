from typing import List, Dict

#########################################
# Recusive Solution
#########################################
def __recursive__(xs: List[str], i: int, dictionary: Dict[str, int]):
    if (i == len(xs)):
        return dictionary

    if (dictionary.get(xs[i])):
        dictionary[xs[i]]+=1
        return __recursive__(xs, i+1, dictionary)
    dictionary[xs[i]]= 1
    return __recursive__(xs, i+1, dictionary)


def excercise45(sentence: str ):
    return __recursive__(sentence.split(' '), 0, dict())

#########################################
# Iterative Solution
#########################################
def other(sentence: str):
    words= sentence.split(" ")
    dictionary= {}
    for word in words:
        if(dictionary.get(word)):
            dictionary[word]+=1
        else:
            dictionary[word]=1
    return dictionary

print(excercise45("lo que no me mata me fortalece"))
print(other("lo que no me mata me fortalece"))

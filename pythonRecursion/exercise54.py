def other(goal: str, letters: list[str]):
    result= []
    current= 0
    for e in goal:
        aux, current= __findBest__(e, letters, current)
        if aux=='impossible':
            return aux
        result.append(aux)
    return result

def __findBest__(e: str, letters: list[str], current: int):
    if (e==letters[current]):
        return "0 here", current

    i= current
    back= 0
    while(i >= 0):
        if (letters[i]==e):
            break
        back+= 1
        i-=1
    else:
        back= len(letters)+1


    j= current
    ahead= 0
    while(j < len(letters)):
        if (letters[j]==e):
            break
        ahead+= 1
        j+=1
    else:
        ahead= len(letters)+1

    if (ahead==back==(len(letters)+1)):
        return 'impossible', -1

    if (back < ahead):
        return f'{back} back', i
    else:
        return f'{ahead} ahead', j

from typing import List

#########################################
# Recursive solution 
#########################################
def mostLargestSubsequence(numbers: List[int], xs: List[int], rs: List[int], num: int, i: int):
    if (i==len(numbers)):
        return rs if (len(rs)>=len(xs)) else xs
    if (num-1==numbers[i]):
        xs.append(numbers[i])
        return mostLargestSubsequence(numbers, xs, rs, numbers[i], i+1)
    else:
        if(len(xs)>len(rs)):
            return mostLargestSubsequence(numbers, [numbers[i]], xs, numbers[i], i+1) 
        else:
            return mostLargestSubsequence(numbers, [numbers[i]], rs, numbers[i], i+1)


def exercise34(numbers: List[int]):
    return mostLargestSubsequence(numbers, [numbers[0]], [], numbers[0], 1) 

#########################################
# Iterative solution 
#########################################
def other(numbers: List[int]):
    n= numbers[0]
    maxLs=[n]
    aux= [n]
    for i in range(1, len(numbers)):
        if(n-1==numbers[i]):
            aux.append(numbers[i])
        else:
            if (len(maxLs)<len(aux)):
                maxLs= aux
            aux= [numbers[i]]
        n= numbers[i]
    return maxLs

print(exercise34([2, 3, 5, 4, 3, 4, 3, 2, 6, 5, 4]))
print(other([2, 3, 5, 4, 3, 4, 3, 2, 1, 6, 5, 4]))
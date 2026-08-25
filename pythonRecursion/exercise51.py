from typing import List

#########################################
# Recusive Solution
#########################################

def __getSpaces__(n: int, r: int):
    if (n < r):
        return n
    return n + __getSpaces__(n - r, r)

def exercise51(matrix: List[List[int]], n: int, index: int= 0):
    if (index == len(matrix) or n == 0):
        return matrix
    spaces= __getSpaces__(n, len(matrix))
    i= spaces % len(matrix[index])
    matrix[index]= matrix[index][len(matrix[index]) - i:] + matrix[index][:len(matrix[index]) - i]
    return exercise51(matrix, n-1, index+1)


#########################################
# Iterative Solution
#########################################

def __getSpacesIterative__(n: int, r: int):
    rs= 0
    while (n > r):
        rs+= n
        n-= r
    return rs+n

def other(matrix: List[List[int]], n: int):
    index= 0

    while (index < len(matrix) or n > 0):
        spaces= __getSpaces__(n, len(matrix))
        i= spaces % len(matrix[index])
        matrix[index]= matrix[index][len(matrix[index]) - i:] + matrix[index][:len(matrix[index]) - i]
        n-= 1
        index+= 1
    return matrix

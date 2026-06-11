
def exercise1(a: int, b: int)->int:
    if (b == 0):
        return 1
    elif (b == 1):
        return a
    
    return a * exercise1(a, b-1)


def other(a: int, b: int):
    return a**b

print(exercise1(2,3))

print(other(2,3))
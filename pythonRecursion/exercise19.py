def exercise19(m: int, n: int):
    if(m==0):
        return n+1
    if(n==0):
        return exercise19(m-1, 1)
    
    return exercise19(m-1, exercise19(m, n-1))


print(exercise19(1,2))
print(exercise19(3,2))
print(exercise19(3,4))
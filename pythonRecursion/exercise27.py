def exercise26(ls: list[int], n: int):
    xs= set(ls)
    xs= list(xs)
    if(n>len(xs)):
        return -1
    return xs[n-1]

print(exercise26([12,7,3,9,1,5,21], 1))
print(exercise26([12,7,3,9,1,5,21], 2))
print(exercise26([12,7,3,9,1,5,21], 5))
print(exercise26([12,7,3,9,1,5,21], 28))
print(exercise26([12,7,3,9,1,5,21], 7))

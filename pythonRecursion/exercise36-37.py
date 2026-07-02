from typing import List

def transpose(histogram: List[str], rs: List[str], i, j):
    if(i==len(histogram)):
        return rs
    
    if (j==len(histogram[i])):
        return transpose(histogram, rs, i+1, 0)

    elem= histogram[i][j]
    rs[j]+= elem
    return transpose(histogram, rs, i, j+1)



def exercise36_37(histogram: List[str]):
    rs=['']*len(histogram[0])
    transpose(histogram, rs, 0, 0)
    return rs


a=['     *', '   ***', '   ***', '  ****', '******' ]
at=exercise36_37(a)
print("\n".join(a))
print("\n".join(at))
#########################################
# Recursive solution
#########################################

class Exercise28:

    def prefix(self, pre: str, word: str, i: int=0, j: int=0):
        if(len(pre)>len(word)):
            return False
        
        if(i==len(pre)):
            return True
        
        if(pre[i]==word[j]):
            return self.prefix(pre, word, i+1, j+1)
        
        return False

    def evaluate(self, suf: str, word: str, i: int, j: int):
        if(i<0):
            return True
        
        if(suf[i] != word[j]):
            return False
        
        return self.evaluate(suf, word, i-1, j-1)


    def sufix(self, suf: str, word: str):
        if(len(suf)>len(word)):
            return False
        
        i= len(suf)-1
        j= len(word)-1

        return self.evaluate(suf, word, i, j)
    
#########################################
# Normal Solution
#########################################
        
class Other: 

    def prefix(self, pre: str, word: str):
        if(len(pre)>len(word)):
            return False
        
        return word[:len(pre)]==pre

    def sufix(self, suf: str, word: str):
        if(len(suf)>len(word)):
            return False
        
        return suf==word[len(word)-len(suf):]
        

#########################################
# Recursive Test
#########################################
        
solution= Exercise28()

print(solution.prefix("Lom", "Lombriz"))
print(solution.prefix("Low", "Lombriz"))
print(solution.sufix("oard", "keyboard"))
print(solution.sufix("add", "keyboard"))

#########################################
# Normal Test
#########################################

solution2= Other()

print(solution2.prefix("Lom", "Lombriz"))
print(solution2.prefix("Low", "Lombriz"))
print(solution2.sufix("oard", "keyboard"))
print(solution2.sufix("add", "keyboard"))

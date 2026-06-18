#########################################
# Recursive Solution
#########################################
class Exercise17:

    def countOcurrences(self, word: str, character: str, ocurrences: int= 0, i: int= 0):
        if(i==len(word)):
            return ocurrences
        if(word[i]==character):
            ocurrences+= 1
        return self.countOcurrences(word, character, ocurrences, i+1)
        

    def reverseWord(self, word: str):
        xs= list(word)
        return self.__processReverseWord__(word=xs, i=0, j=len(xs)-1)

    def __processReverseWord__(self, word: list[str], i: int, j: int ):
        if(i==j):
            return "".join(word)
        
        aux= word[j]
        word[j] = word[i]
        word[i] = aux
        return self.__processReverseWord__(word, i+1, j-1)


    def countVowels(self, word: str, numVowels: int= 0, i: int= 0):
        if(i==len(word)):
            return numVowels
        if(word[i] in "aeiouAEIOU"):
            numVowels= numVowels+1
        return self.countVowels(word, numVowels, i+1)
    
#########################################
# Iterative Solution
#########################################
class Other:
    
    def countOcurrences(self, word: str, character: str):
        ocurrences= 0
        for c in word:
            if(c==character):
                ocurrences+=1
        return ocurrences
        
    def reverseWord(self, word: str):
        # xs= list(word)
        # xs.reverse()
        # return "".join(xs)
        return word[::-1]
    
    def countVowels(self, word: str):
        numVowels= 0

        for c in word:
            if(c in "aeiouAEIOU"):
                numVowels+= 1    

        return numVowels


#########################################
# Recursive Test
#########################################
e= Exercise17()
print(e.countOcurrences("elementos de programacion", "e"))
print(e.reverseWord("comer"))
print(e.countVowels("elementos de programacion"))

#########################################
# Iterative Test
#########################################
e2= Other()
print(e2.countOcurrences("elementos de programacion", "e"))
print(e2.reverseWord("comer"))
print(e2.countVowels("elementos de programacion"))
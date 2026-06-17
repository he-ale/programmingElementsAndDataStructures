from typing import Optional

from exercise2 import exercise2

class Node:
    data: int
    next: Optional['Node']= None

    def __init__(self, data: int):
        self.data= data

class Sequence:
    head: Optional[Node]=None
    last: Optional[Node]=None
    size: int= 0

    #################################
    # Excercise 5
    #################################
    def __init__(self, data: Optional[int]= None, *args):
        if data is None:
            self.size=0
        else:
            self.head= Node(data)
            self.last= self.head
            self.size=1
            for e in args:
                self.append(e)

    def append(self, data: int):
        self.last.next= Node(data)
        self.last= self.last.next
        self.size= self.size+1

    #################################
    # Excercise 6
    #################################

    def sum(self):
        current= self.head
        result= 0
        while current:
            result= result+current.data
            current=current.next
        return result

    #################################
    # Excercise 7
    #################################

    def minValue(self):
        current= self.head.next
        result= self.head.data
        while current:
            result= min(result, current.data)
            current= current.next
        return result

    #################################
    # Excercise 9
    #################################
    
    def find(self, target: int):
        current= self.head
        index= -1
        while current:
            if(current.data==target):
                return (index+1, current.data)
            current= current.next
            index= index+1
        return (-1, None)
    
    #################################
    # Excercise 10
    #################################

    def map(self, function):
        current= self.head
        newList= Sequence(function(current.data))
        current= current.next
        while current:
            newList.append(function(current.data))
            current= current.next
        return newList

    #################################
    # Excercise 11
    #################################

    def sumList(self, otherList: 'Sequence'):
        if(otherList.size==self.size):
            current= self.head
            other=otherList.head
            while(current and other):
                current.data= current.data+other.data
                other= other.next
                current= current.next
        else:
            raise ValueError("List doen't match")
        
    #################################
    # Excercise 12
    #################################
    
    def escalarProduct(self, otherList: 'Sequence'):
        result=0
        if(self.size== otherList.size):
            current1= self.head
            current2= otherList.head

            while(current2 and current1):
                result= (current1.data*current2.data)+result
                current1= current1.next
                current2= current2.next

            return result
        else:
            raise ValueError("List doesn't match")

    #################################
    # Excercise 13
    ################################# 
    def sumPrimes(self):
        result=0
        current= self.head

        while current:
            if(exercise2(current.data)):
                result= result+current.data
            current= current.next
        return result

    def __iter__(self):
        current= self.head
        while current:
            yield current.data
            current= current.next

    def __str__(self):
        current= self.head
        result="["
        while current:
            result=result+str(current.data)+" "
            current= current.next

        return result.strip()+"]"


sequence= Sequence(1,2,3)
sequence2= Sequence(1,2,3)

print(sequence.sum())
print(sequence.minValue())
print(sequence.find(2))
print(sequence.find(5))
sequence.sumList(sequence2)
print(str(sequence))
print(sequence.escalarProduct(sequence2))


sequence3= Sequence(1,2,3, 8, 23, 9)
print(sequence3.sumPrimes())

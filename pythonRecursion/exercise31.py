class Exercise31:

    bills= [100, 50, 20, 10, 5, 2, 1]
    cents= [50, 25, 10, 5, 1]


    def __getCents__(self, amount:int, i=0, counter= 0):
        if 0<=amount<1:
            if counter==0:
                return ""
        
        if(self.cents[i]>amount):
            return self.__getCents__(amount, i+1, 0)
        
        amount-=self.cents[i]
        counter+=1

        if(amount<self.cents[i]):
            return str(counter)+":"+str(self.cents[i])+"cents "+self.__getCents__(amount, i+1, 0)
        
        return self.__getCents__(amount, i, counter)
        
    def equivalent(self, amount, i= 0, counter= 0):
        if(0<=amount<1):
            if counter==0:
                return self.__getCents__(amount*100)
            return str(counter)+":"+str(self.bills[i])+ " "+ self.__getCents__((amount*100)//1)

        if(self.bills[i]>amount):
            return self.equivalent(amount, i+1)
        
        amount= amount-self.bills[i]
        counter+=1
        if(amount<self.bills[i]):
            return str(counter)+":"+str(self.bills[i])+"$ " + self.equivalent(amount, i+1, 0)
        
        return self.equivalent(amount, i, counter)




class Other:

    bills= [100, 50, 20, 10, 5, 2, 1]
    cents= [50, 25, 10, 5, 1]

    def __getCents__(self, amount):
        pass
    
    def equivalent(self, amount):
        i= 0
        counter= 0
        res= ""
        while 1<=amount:
            if(self.bills[i]>amount):
                if(counter>0):
                    res= res+ str(counter)+":"+ str(self.bills[i])+"$ "
                    counter=0
                i+=1
            else:
                amount-=self.bills[i]
                counter+=1
        
        if counter>0:
            res= res+ str(counter)+":"+ str(self.bills[i])+"$ "
        
        amount=(amount*100)//1
        counter= 0
        i=0

        while 0 < amount:
            if(self.cents[i]>amount):
                if(counter>0):
                    res= res+ str(counter)+":"+ str(self.cents[i])+"cents "
                    counter=0
                i+=1
            else:
                amount-=self.cents[i]
                counter+=1
        if counter>0:
            res= res+ str(counter)+":"+ str(self.bills[i])+"cents "
        return res

e31= Exercise31()
print(e31.equivalent(233.80))

o31= Other()
print(o31.equivalent(233.80))

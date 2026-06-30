#########################################
# Recursive solution 
#########################################

class Exercise31:

    bills= [100, 50, 20, 10, 5, 2, 1]
    cents= [50, 25, 10, 5, 1]

    def __fractionate__(self, amount, xs, prefix, i=0, counter= 0):
        if(0<=amount<1):
            if prefix=='cents':
                return ""
            if counter==0:
                return self.__fractionate__(amount*100, self.cents, 'cents', 0, 0)
            return str(counter)+":"+str(xs[i])+ prefix+" "+ self.__fractionate__(amount*100, self.cents, 'cents', 0, 0)

        if(xs[i]>amount):
            return self.__fractionate__(amount, xs, prefix, i+1, 0)
        
        amount= amount-xs[i]
        counter+=1
        if(amount<xs[i]):
            return str(counter)+":"+str(xs[i])+prefix+" " + self.__fractionate__(amount, xs, prefix, i+1, 0)
        
        return self.__fractionate__(amount, xs, prefix, i, counter)


    def equivalent(self, amount, i= 0, counter= 0):
        return self.__fractionate__(amount, self.bills, '$', 0, 0)

#########################################
# Iterative solution 
#########################################

class Other:

    bills= [100, 50, 20, 10, 5, 2, 1]
    cents= [50, 25, 10, 5, 1]

    def __fractionate__(self, amount, xs, prefix):
        i= 0
        counter= 0
        res= ""
        while 1<=amount:
            if(xs[i]>amount):
                if(counter>0):
                    res= f"{res}{counter}:{xs[i]}{prefix} "
                    counter=0
                i+=1
            else:
                amount-=xs[i]
                counter+=1
        
        if counter>0:
            res= f"{res}{counter}:{xs[i]}{prefix} "
        return (res, amount)   
         
    
    def equivalent(self, amount):
        res, amount= self.__fractionate__(amount, self.bills, '$')
               
        amount=(amount*100)//1
        res2, _= self.__fractionate__(amount, self.cents, 'cents')

        return f"{res}{res2}"

e31= Exercise31()
print(e31.equivalent(233.80))

o31= Other()
print(o31.equivalent(233.80))

#########################################
# Recusive Solution
#########################################

def exercise52(x: int):
    if (x == 1):
        return 1

    if(x % 2 == 0):
        return x + exercise52(x//2)
    
    return x + exercise52((x * 3) + 1)

#########################################
# Iterative Solution
#########################################

def other(x: int):
    messagesSent= 0
    while (x != 1):
        messagesSent+= x
        if (x%2 == 0):
            x= x//2
        else:
            x= (x*3) + 1

    return messagesSent + 1

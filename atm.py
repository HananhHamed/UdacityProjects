moneyList=[100,50,10,5,2]
def printData(money,count):
    while(count>0):
        print "give "+ str(money)
        count=count-1

def ATM (money):
    i=0
    while(i<len(moneyList)):
        if money>=moneyList[i]:
            x=int(money/moneyList[i])
            printData(moneyList[i],x)
            money=money-x*moneyList[i]
            if(money<moneyList[-1]):
                print "give", money
                break
            i=i+1
        else:
            i=i+1

ATM(273)

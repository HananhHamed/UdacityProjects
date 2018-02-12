class ATM:
    def __init__(self, balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawal_list = []
    moneyList = [100 , 50 , 10 , 5]
    #create printdata function to help withdraw function
    def printData(self , money , count):
        while(count > 0):
            print "give " + str(money)
            count = count-1
    #create withdraw function
    def withdraw (self , request):
        print "Welcome to " + self.bank_name
        print "Current Balance = " + str(self.balance)
        print "========================="
        if ( request < self.balance ):
            self.balance = self.balance - request
            self.withdrawal_list.append( request )
            i=0
            while( i < len( self.moneyList ) ):
                if ( request >= self.moneyList[i] ):
                    x = int(request / self.moneyList[i])
                    self.printData ( self.moneyList[i] , x )
                    request = request - x * self.moneyList[i]
                    if ( request < self.moneyList[-1] ):
                        print "give ", request
                        break
                    i = i + 1
                else:
                    i = i + 1
        else:
            print "Can't give you all this money !!"
    #create show_withdrawals function
    def show_withdrawals( self ):
        print "Your Last Withdrawals: "
        for withdrawal in self.withdrawal_list:
             print withdrawal 

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(120)
atm1.show_withdrawals()

#atm2.withdraw(100)
#atm2.withdraw(2000)

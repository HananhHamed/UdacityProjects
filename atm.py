class ATM:
    def __init__(self, balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawal_list = []

    '''create withdraw function'''
    def withdraw (self , request ):
        print "Welcome to " + self.bank_name
        print "Current Balance = " + str(self.balance)
        print "========================="
        if request < self.balance:
            moneyList = [100 , 50 , 10 , 5]
            self.balance = self.balance - request
            self.withdrawal_list.append( request )
            i=0
            count=0
            while i < len(moneyList):
                if request >= moneyList[i]:
                    x = int(request / moneyList[i])
                    count = x
                    while count > 0:
                        print "give " + str(moneyList[i])
                        count =count - 1
                    request = request - x * moneyList[i]
                    if request < moneyList[-1]:
                        print "give ", request
                        break
                    i = i + 1
                else
                    i = i + 1
        elif request > self.balance
            print "Can't give you all this money !!"
        else:
            print "More than 0 please!!!"

    '''create show_withdrawals function'''
    def show_withdrawals(self):
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

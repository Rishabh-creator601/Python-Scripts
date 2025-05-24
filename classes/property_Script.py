

class Bank :
    def __init__(self):
        self.account_name  =  "AndaPAisa"
        self.__password  = 1234  # Now becomes private 
        self.tip = 0.1
        self.balance  = 9000
    
    @property
    def discount(self):
        print(self.balance - (self.balance * self.tip))
        
        

bank = Bank()
bank.discount
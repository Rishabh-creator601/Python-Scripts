


'''
__repr__ and __str__ are exchangbly used BUT,
repr is aimed at programmer 
str is aimed at user

'''


class Bank :
    def __init__(self):
        self.account_name  =  "AndaPAisa"
        self._password  = 1234
    
    def __repr__(self):
        return f"<{self.account_name}> REPR"
    
    # def __str__(self):
    #     return f"<{self.account_name}> STR"
    


bank = Bank()



print(str(bank))


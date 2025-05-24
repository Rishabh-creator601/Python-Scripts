class Bank :
    def __init__(self):
        self.account_name  =  "AndaPAisa"
        self.__password  = 1234  # Now becomes private 



print(Bank().account_name) # AndaPAisa 
print(Bank().__password) # error 
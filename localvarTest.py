class Account:
    num_account = 0
    def __init__(self, name):
        self.name = name
        Account.num_account +=1
    def __del__(self):
        Account.num_account -=1

a = Account('aa')
b = Account('bb')




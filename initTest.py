class initTest:

    def __init__(self, a, b):
        self.name = a
        self.age = b

    def getInfo(self) :
        print(self.name + str(self.age))


test = initTest("park", 200)
test.getInfo()

class payTest:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -=amount
        print(str(self.__wallet))

test = payTest('park', 99, 'aaa', 10000)
print(str(test.age))

test.pay(4000)
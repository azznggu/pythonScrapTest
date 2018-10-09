class Test:
    def setInfo(self, a, b):
        self.name = a
        self.age = b

    def getInfo(self):
        print(self.name + " "+ str(self.age))



test = Test()
test.setInfo("aaa", 99)

test.getInfo()
        

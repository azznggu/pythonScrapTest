class parent:
    def __init__(self, a, b):
        self.a = a
        self.b= b

    def add(self):
        result = self.a+self.b
        return result

pTest = parent(10,20)
print(pTest.add())

class child(parent):
    def add(self):
        result = 2*(self.a+self.b)
        return result

cTest = child(10,20)
print(cTest.add())




class MyMatrix(object):
    def __init__(self,list):
        self.list = list

    def __add__(self,other):
        
        return [self.list[0] + other[0],self.list[1] + other[1],self.list[2] + other[2],self.list[3] + other[3]]

a = MyMatrix([1,2,3,4])
b = a.__add__([5,6,7,8])
print(b)

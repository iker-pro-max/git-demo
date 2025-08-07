
def quick_sort(a):
    if len(a) <= 1:
        return a
    left = []
    right = []
    for i in range(len(a)):
        if i == 1:
            continue
        if a[i] <= a[1]:
            left.append(a[i])
        if a[i] > a[1]:
            right.append(a[i])
    return quick_sort(left) +[a[1]] +quick_sort(right)

class Mylist(object):
    def __init__(self,init):
        self.init = init
        

    def Len(self):
        count = 0
        for i in self.init:
            count += 1
        print(count)
    
    def Append(self,added):
        for i in added:
            self.init += [i] 
        print(self.init)
    
    def Index(self,index):
        number = -1
        for i in self.init:
            number += 1
            if number == index:
                break
        print(i)

    def Sort(self):
        s = quick_sort(self.init)
        print(s)
        
        
a = Mylist([4,1,3,2])

a.Sort()
a.Len()
a.Index(2)
a.Append([3,4])


    























# a = [2,1,4,3]
# b = a

# def test(tmp, t):
#     tmp[0] = t

# print(a)
# test(a, 0)
# print(a)
# test(b, 4)
# print(a)


# class MyClass():
#     def __init__(self, a):
#         self.a =a


# b = MyClass(3)
# print(b.a)

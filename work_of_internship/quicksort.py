a = []
def qs(a):
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
    return qs(left) +[a[1]] +qs(right)


a = [1,3,9,3,2,1,-1,5,294,7]
b = qs(a)
print(b)

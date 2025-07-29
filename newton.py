a=float((input("输入a:")))
b=float((input("输入b:")))
c=float((input("输入c:")))
m=0.00000001
x=10

def f(x):
    return a*x**2+b*x+c
def df(x):
    return 2*a*x+b

f_x=f(x)
df_x=df(x)

x1=x-f_x/df_x

if a == 0:
    if b == 0:
        if c == 0:
            print("所有实数都是解")
        else:
            print("无解")
    else:
        solution = -c / b
        print(f"解为: {solution}")
else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("无实数解")
    else:
        while(abs(x1-x)>=m):
            x=x1
            x1=x-f_x/df_x
  
            break

        x2=-b/a-x1

        print(f"解为：{x1},{x2}")


def newton_recursion_method(a,b,c,x0,tolerance=0.0001,max_recursion_depth=100,recursion_depth=0):
    
    f_x0 =  a*x0**2 + b*x0 + c
    df_x0 = 2*a*x0 + b
    x1 = x0 - f_x0/df_x0
    if recursion_depth >= max_recursion_depth:
        return x0
    else:
        if abs(x1-x0) < tolerance:
            return x1
        else:
            return newton_recursion_method(a,b,c,x1,tolerance=0.0001,max_recursion_depth=100,recursion_depth=recursion_depth+1)
       

if __name__ == "__main__":
    print("===== 牛顿递归法求二次方程根 =====")

    a = float(input("输入二次项系数 a: "))
    b = float(input("输入一次项系数 b: "))
    c = float(input("输入常数项 c: "))
    x0 = float(input("输入初始猜测值 x0: "))        
       
    result = newton_recursion_method(a, b, c, x0)
    
    print("该一元二次方程的一个根为："+str(result)) 
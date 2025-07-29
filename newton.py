def newton_method(a, b, c, x0, tol=1e-7, max_iter=100):
    """
    使用牛顿法求解二次方程 ax^2 + bx + c = 0 的根
    
    参数:
        a, b, c (float): 二次方程的系数
        x0 (float): 初始猜测值
        tol (float): 容差（默认1e-7）
        max_iter (int): 最大迭代次数（默认100）
        
    返回:
        float: 找到的根
        None: 如果达到最大迭代次数仍未收敛
    """
    # 定义函数及其导数
    def f(x):
        return a * x**2 + b * x + c
        
    def df(x):
        return 2 * a * x + b
        
    # 牛顿法迭代
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        # 检查导数是否为零
        if abs(dfx) < tol:
            break
            
        # 牛顿法更新公式
        x_new = x - fx / dfx
        
        # 检查收敛条件
        if abs(x_new - x) < tol:
            return x_new
            
        x = x_new
        
    return None

def find_roots(a, b, c):
    """
    寻找二次方程 ax^2 + bx + c = 0 的所有实根
    
    参数:
        a, b, c (float): 二次方程的系数
        
    返回:
        list: 包含所有实根的列表（可能为0, 1或2个根）
    """
    # 处理非二次方程的情况
    if a == 0:
        if b == 0:
            return [] if c != 0 else ["无穷解"]
        return [-c / b]
    
    discriminant = b**2 - 4 * a * c
    
    # 无实根
    if discriminant < 0:
        return []
    
    # 计算对称轴作为初始点参考
    vertex = -b / (2 * a)
    
    # 尝试不同的初始点
    roots = set()
    
    # 尝试对称轴附近的点
    initial_points = [vertex + 5, vertex - 5, vertex + 1, vertex - 1, 0]
    
    for x0 in initial_points:
        root = newton_method(a, b, c, x0)
        if root is not None:
            # 验证找到的根是否满足方程
            if abs(a * root**2 + b * root + c) < 1e-5:
                roots.add(round(root, 8))  # 四舍五入到8位小数
    
    # 按数值大小排序
    return sorted(roots)

# 获取用户输入
print("求解二次方程 ax^2 + bx + c = 0")
a = float(input("输入系数 a: "))
b = float(input("输入系数 b: "))
c = float(input("输入系数 c: "))

print("hello world")

# 计算并显示结果
roots = find_roots(a, b, c)
if not roots:
    print("方程没有实根")
else:
    print("找到的实根:", ", ".join(map(str, roots)))

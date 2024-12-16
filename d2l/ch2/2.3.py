## 线性代数
# 标量 
# 标量由一个元素的张量表示
import torch
x = torch.tensor(3.0)
y = torch.tensor(2.0)
print(x + y, "\t", x * y, "\t", x / y,"\t",x ** y)

# 向量
# 向量可以被视为标量值组成的列表
x = torch.arange(4)
print("\n", x)
# 我们可以使用下标来引用向量的任一个元素
print("\n", x[3])
print("\n", len(x))
# 当用张量表示一个向量时，张量只有一个轴，使用shape属性来获取张量形状
# 为一个元素组
print("\n", x.shape)

# 矩阵
# 向量将标量从零阶推广到一阶，矩阵将向量从一阶推广到二阶
# 当矩阵具有相同数量的行和列时，其形状将变为正方形；
# 因此，它被称为方阵（square matrix）
A = torch.arange(20).reshape(5,4)
print("\n", A)
# 访问矩阵的转置
print("\n", A.T)
# 对称矩阵转置与原始矩阵相同
B = torch.tensor([[1,2,3], [2,0,4], [3,4,5]])
print("\n", B)
if torch.all(B == B.T):
    print("\n", B.T)
print("\n", B == B.T)

# 张量
# 张量是描述具有任意数量轴的n维数组的通用方法
X = torch.arange(24).reshape(2,3,4)
print("\n", X)
A = torch.arange(20, dtype=torch.float32).reshape(5,4)
B = A.clone() # 通过分配新内存，将A的一个副本分配到B
print("\n", A, "\n", A + B)
print("\n", A * B)
# 将张量乘以或加上一个标量不会改变张量的形状，
# 其中张量的每个元素都将与标量相加第三的或相乘
a = 2
X = torch.arange(24).reshape(2,3,4)
print("\n", a+X, "\n", (a * X).shape)
# 降维
# 我们可以对任意张量进行的一个有用的操作是计算其
# 所有元素的总和
x = torch.arange(4, dtype=torch.float32)
print("\n", x, "\t", x.sum())
print("\n", A.shape, "\t", A.sum())
# 默认情况下，调用求和函数会沿所有的轴降低张量的维度，使它变为一个标量。
# 我们还可以指定张量沿哪一个轴来通过求和降低维度。
A_sum_axis0 = A.sum(axis=0)
print("\n", A_sum_axis0, "\t", A_sum_axis0.shape)
# 指定axis=1将通过汇总所有列的元素降维（轴1）。因此，输入轴1的维数在输出形状中消失
A_sum_axis1 = A.sum(axis=1)
print("\n", A_sum_axis1, "\t", A_sum_axis1.shape)
# 沿着行和列对矩阵求和，等价于对矩阵的所有元素进行求和
A.sum(axis=[0, 1]) # 结果和A.sum()一样
print("\n", A.sum(axis=[0, 1]))
# 与求和相关的量是平均值（mean或average）。我们通过将总和除以元素总数来计算平均值
print("\n", A.mean(), "\t", A.sum() / A.numel())
# 同样，计算平均值的函数也可以沿指定轴降低张量的维度。
print("\n", A.mean(axis=0),"\t", A.sum(axis=0) / A.shape[0])

# 非降维求和
# 有时在调用函数来计算总和或均值时保持轴数不变会很有用
sum_A = A.sum(axis=1, keepdims=True)
print("\n", sum_A, "\n", A / sum_A)
# 如果我们想沿某个轴计算A元素的累积总和，比如axis=0（按行计算）
# ，可以调用cumsum函数。此函数不会沿任何轴降低输入张量的维度。
print("\n", A.cumsum(axis=0))

# 点积
y = torch.ones(4, dtype=torch.float32)
print("\n", x, "\t", y, "\t", torch.dot(x, y))
# 也可以通过执行元素乘法，然后进行求和来表示两个向量的点积
print("\n", torch.sum(x * y))

# 矩阵-向量积
# 在代码中使用张量表示矩阵-向量积，我们使用mv函数,
# 当我们为矩阵和向量x调用torch.mv时，会执行矩阵-向量积
# 注意，a的列维数（沿轴1的长度）必须与x的维数相同
print("\n", A.shape, "\t", x.shape, "\t",torch.mv(A, x))

# 矩阵-矩阵乘法
B = torch.ones(4,3)
print("\n", A.shape, "\n", B.shape, "\n", torch.mm(A,B))

# 范数
# 线性代数中最有用的一些运算符是范数（norm）。
# 非正式地说，向量的范数是表示一个向量有多大。
# 这里考虑的大小（size）概念不涉及维度，而是分量的大小。
u = torch.tensor([3.0,-4.0])
print("\n", torch.norm(u))
# 深度学习中更经常地使用L2 范数的平方，也会经常遇到L1 范数，
# 它表示为向量元素的绝对值之和：
torch.abs(u).sum()
print("\n", torch.abs(u).sum())
# Frobenius范数满足向量范数的所有性质，它就像是矩阵形向量的L2 范数。
Frobenius = torch.norm(torch.ones((4,9)))
print("\n", Frobenius)
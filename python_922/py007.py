import torch
from  torch import tensor

########tensor
x = tensor(42,)
print(x)

x.dim()

2*x
x.item()
############vector
v = tensor([1.5,-0.5,3.0])
print(v)

v.dim()

v.size()

##########matrix
M  = tensor([[1,3],[5,4]])
print(M)

M.matmul(M)

tensor([1,0]).matmul(M)

M * M  #矩阵对应数相乘

tensor([1,2]).matmul(M)









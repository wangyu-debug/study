import torch
print(torch.__version__)

x = torch.empty(5,3)
#随机数
x = torch.rand(5,3)
x
# 全零
x = torch.zeros(5,3)
x
##构建一样大小的矩阵
x = x.new_ones(5,3,dtype=torch.double)
x = torch.rand_like(x,dtype=torch.double)
x
##展示矩阵大小
x.size()
##reshape
x = torch.randn(4,4)
y = x.view(16)
z = x.view(-1,8) #-1表示的是自动计算
print(x.size(),y.size(),z.size())
#与numpy的协同操作
import numpy as np
a = torch.ones(5)
b = a.numpy()
print(b)

a = np.ones(5)
b = torch.from_numpy(a)
print(b)








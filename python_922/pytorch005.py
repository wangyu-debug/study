## 自动求导机制

import torch
x = torch.randn(3,4,requires_grad=True)
b = torch.randn(3,4,requires_grad=True)
print(b)

t = x + b
y = t.sum()

y.backward()  #调用反向传播 然后再进行求导
b.grad  #对b求导
print(b.grad)

##计算流程
x = torch.randn(1,requires_grad=True)
b = torch.randn(1,requires_grad=True)
w = torch.randn(1,requires_grad=True)
y = w * x
z = y + b
#进行反向传播
z.backward(retain_graph=True) #若清空的话，再执行反向传播代码及求导之后会累加的
print(w.grad)
print(b.grad)

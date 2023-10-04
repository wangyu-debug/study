import torch
import torch.nn as nn
import numpy as np


x_values = [i for i in range(11)]
x_train = np.array(x_values,dtype = np.float32)
x_train = x_train.reshape(-1,1)
print(x_train.shape)

y_values = [2*i+1 for i in x_values]
y_train = np.array(y_values,dtype=np.float32)
y_train = y_train.reshape(-1,1)
print(y_train.shape)

###线性回归是不加激活函数的全连接层
class LinearRegressionModel(nn.Module): #从nn.Module继承
    def __init__(self,input_dim,output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim,output_dim)
    def forward(self,x):
        out = self.linear(x)
        return out
input_dim = 1
output_dim = 1
model = LinearRegressionModel(input_dim,output_dim)
print(model)
##指定好参数和损失函数
epochs = 1000
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
criterion = nn.MSELoss()

#训练模型
for epoch in range(epochs):
    epoch += 1

    #更换参数格式
    inputs = torch.from_numpy(x_train)
    labels = torch.from_numpy(y_train)

    #梯度要清零每一次迭代
    optimizer.zero_grad()

    #前向传播
    outputs = model(inputs)

    #计算损失
    loss = criterion(outputs,labels)

    #反向传播
    loss.backward()

    #更新权重参数
    optimizer.step()

    if epoch % 50 ==0:
        print("epoch {},loss {}".format(epoch,loss.item()))



predicted = model(torch.from_numpy(x_train).requires_grad_()).data.numpy()
print(predicted)

#模型的保存与提取
torch.save(model.state_dict(),'model.pkl')  ##模型的权重参数
model.load_state_dict(torch.load('model.pkl'))


###################################使用GPU训练 ：将数据和模型传入到cuda中
class LinearRegressionModel(nn.Module): #从nn.Module继承
    def __init__(self,input_dim,output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim,output_dim)
    def forward(self,x):
        out = self.linear(x)
        return out
input_dim = 1
output_dim = 1
model = LinearRegressionModel(input_dim,output_dim)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

print(model)
##指定好参数和损失函数
epochs = 1000
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
criterion = nn.MSELoss()

#训练模型
for epoch in range(epochs):
    epoch += 1

    #更换参数格式
    inputs = torch.from_numpy(x_train).to(device)
    labels = torch.from_numpy(y_train).to(device)

    #梯度要清零每一次迭代
    optimizer.zero_grad()

    #前向传播
    outputs = model(inputs)

    #计算损失
    loss = criterion(outputs,labels)

    #反向传播
    loss.backward()

    #更新权重参数
    optimizer.step()

    if epoch % 50 ==0:
        print("epoch {},loss {}".format(epoch,loss.item()))













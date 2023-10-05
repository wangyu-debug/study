#numpy 是列表
#pandas 字典

import pandas as pd
import numpy as np

s = pd.Series([1,23,4,np.nan])
print(s)

dates = pd.date_range("20231004",periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.random.randn(12).reshape((3,4)))
print(df1)

df2 = pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20231004'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["TEST","test","ete","sdsd"]),
    'F':'foo'
})
print(df2)
print(df2.dtypes)
print(df2.index)    #行
print(df2.columns)  #列
print(df2.values)  #每一个值
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values('E'))


##选择数据
dates = pd.date_range('20231005',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)

print(df['A'],"\n",df.A)
print(df[0:3],"\n",df['20231005':'20231007'])

print(df.loc['20231005'])
print(df.loc[:,['A','B']])
print(df.loc['20231007':,['A','B']])

print(df.iloc[2,2])  #类似numpy
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])

print(df[df.A>8]) #筛选


###设置值
dates = pd.date_range('20231005',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)

df.iloc[2,2] = 111
print(df)

df.loc['20231005','B'] = 5555
print(df)

df[df.A>4] = 0
print(df)

df.A[df.A>4] = 0
print(df)

df.B[df.A>4] = 0
print(df)

df['F'] = np.nan
print(df)

df['E'] = pd.Series([1,2,3,43,5,6],index=pd.date_range('20231005',periods=6))
print(df)


##处理丢失值
dates = pd.date_range('20231005',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

print(df.dropna(axis=0,how='any'))  #how = 'all'
print(df.dropna(axis=1,how='any'))  #how = 'all'

print(df.fillna(value=0))

print(df.isnull().sum())
print(np.any(df.isnull==True))


###导入导出
data = pd.read_csv("B:/python_torch/study/mofan/numpy_and_pandas/data.csv")
print(data)

data.to_csv("mytest.csv")

###合并concat
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
print(df1)
print(df2)
print(df3)

#concat
print(pd.concat([df1,df2,df3],axis=0,ignore_index=True))


#join
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['E','F','C','D'],index=[3,2,4])
print(df1)
print(df2)

print(pd.concat([df1,df2],join='outer'))
print(pd.concat([df1,df2],join='inner',ignore_index=True))  ##相同部分合并 列

##append  上下
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*3,columns=['A','B','C','D'])
print(df1.append(df2,ignore_index=True))
print(df1.append([df2,df3],ignore_index=True))

s1 = pd.Series([1,2,3,4],index=['A','B','C','D'])
print(df1.append(s1,ignore_index=True))

#### merge 合并
###单个key
left = pd.DataFrame({
    'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right = pd.DataFrame({
'key':['k0','k1','k2','k3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})
print(left)
print(right)

print(pd.merge(left,right,on='key'))

##多个key
left = pd.DataFrame({
    'key1':['k0','k0','k1','k2'],
    'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right = pd.DataFrame({
    'key1':['k0','k1','k1','k2'],
    'key':['k0','k1','k2','k3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})
print(left)
print(right)
print(pd.merge(left,right,on=['key','key1']))
print(pd.merge(left,right,on=['key','key1'],how="outer"))
print(pd.merge(left,right,on=['key','key1'],how="inner"))
print(pd.merge(left,right,on=['key','key1'],how="right"))
print(pd.merge(left,right,on=['key','key1'],how="left"))


##indicator
df1 = pd.DataFrame({
    'col1':[0,1],
    'col_left':['a','b']
})
df2 = pd.DataFrame({
    'col1':[1,2,3],
    'col_right':[2,2,2]
})
print(df1)
print(df2)
print(pd.merge(df1,df2,on='col1',how="outer",indicator=True))

##index
left = pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0','B1','B2']},
    index=['k0','k1','k2']
)
right = pd.DataFrame({
    'C':['C0','C1','C2'],
    'D':['D0','D1','D2']},
    index=['k0','k3','k2']
)
print(left)
print(right)
print(pd.merge(left,right,left_index=True,right_index=True,how="outer"))

#suffixes
boys = pd.DataFrame({
    'k':['k0','k1','k2'],
    'age':[1,2,3]
})
girls = pd.DataFrame({
    'k':['k0','k0','k2'],
    'age':[4,5,6,]
})
print(boys)
print(girls)

print(pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how="outer"))
print(pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how="inner"))


##plot
import matplotlib.pyplot as plt
##series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()


##dataframe
data  = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data  = data.cumsum()
ax = data.plot.scatter(x='A',y='B',color="DarkBlue",label="Class 1")
ax1 = data.plot.scatter(x='A',y='C',color="DarkGreen",label="Class 2",ax=ax)
plt.show()










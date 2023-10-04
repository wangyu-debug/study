import  numpy as np
##基于矩阵的运算
array = np.array([[1,2,3],[4,5,6]])
print(array)
print("dim: ",array.ndim)
print("shape:" ,array.shape)
print("size:",array.size)

##numpy 的创建
a = np.array([2,2,3,2],dtype=np.int)
print(a)
print(a.dtype)
a = np.array([2,2,3,2],dtype=np.float32)
print(a.dtype)

b = np.array([[2,1,2,3],[2,4,5,2]])
print(b)

c = np.zeros((3,4))
print(c)

d = np.ones((3,4),dtype=np.float32)
print(d)

e = np.arange(10,20,2)
print(e)

f = np.arange(12).reshape((3,4))
print(f)

g = np.linspace(1,10,6).reshape((2,3))
print(g)

###基础运算
a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)
print("=====")
c = a-b
d = a+b
e = b**2
print(c)
print("=====")
print(d)
print("=====")
print(e)

g = 10*np.sin(a)
print(g)

print(b==3)

##矩阵的运算
aa = np.array([[1,1],[2,2]])   #对应相乘
bb = np.arange(4).reshape((2,2)) #矩阵相乘

print(aa*bb)
print(np.dot(aa,bb))
print(a.dot(b))

##创建随机
a = np.random.random((2,4))
print(a)
#[[0.88179376 0.41286831 0.60984712 0.31970794]
# [0.66830859 0.82961354 0.86752349 0.58338086]]
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.sum(a,axis=1))  #[2.22421714 2.94882648]
print(np.min(a,axis=1)) #[0.31970794 0.58338086]

###基础运算2
A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))  #0 index min
print(np.argmax(A))  #11  index max
print(np.mean(A))  #7.5
print(np.median(A))
print(np.cumsum(A))  #[ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.diff(A))  #[[1 1 1]
                    # [1 1 1]
                    # [1 1 1]]
print(np.nonzero(A))  #(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
print(np.sort(A))  #逐行排序
print(np.transpose(A))  #转置
print(np.clip(A,5,9))
print(np.mean(A,axis=1))  #[ 3.5  7.5 11.5]


##索引
A = np.arange(3,15)
print(A) #[ 3  4  5  6  7  8  9 10 11 12 13 14]
print(A[3])
A = np.arange(3,15).reshape((3,4))
print(A[2])
print(A[2][2])  #13
print(A[2,2])   #13
print(A[2,:]) #[11 12 13 14] 第三行
print(A[:,1]) #[ 4  8 12]  第二列

##迭代行
for row in A:
    print(row)
##迭代列
for col in A.T:
    print(col)
##迭代每一项
print(A.flatten())
for item in A.flat:
    print(item)


##array的合并
A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack((A,B))
print(np.vstack((A,B)))  #[[1 1 1]
                        # [2 2 2]]
print(A.shape,C.shape)  #(3,) (2, 3)

D = np.hstack((A,B))
print(np.hstack((A,B)))  #[1 1 1 2 2 2]

print(A[np.newaxis,:])  #[[1 1 1]]
print(A[:,np.newaxis])  #[[1]
                        # [1]
                        # [1]]

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(np.hstack((A,B)))

C = np.concatenate((A,B,B,A),axis=0)
print(C)


###array 分割
A = np.arange(12).reshape(3,4)
print(A)

#等分割
print(np.split(A,2,axis=1))
print(np.split(A,3,axis=0))

print(np.vsplit(A,3))
print(np.hsplit(A,2))

#不等分割
print(np.array_split(A,3,axis=1))


###copy deepcopy
a = np.arange(4)
b = a
c = a
d = b

a[0] = 11
print(a)
print(b is a)
print(c is a)
print(d is a)

d[1:3] = [22,33]
print(a)
b = a.copy()   #没有关联
a[0] = 0
print(a)  #[ 0 22 33  3]
print(b)  #[11 22 33  3]




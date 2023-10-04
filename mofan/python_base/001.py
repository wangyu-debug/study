print("hello world")

print("hello"+str(222))

1+1

4**2

#取余
8%3

#取整
9//4

a,b,c = 5,5,5
print(a,b,c)

###while循环
condition = 1
while condition <= 10:
    print(condition)
    condition += 1

###for循环
exanmple_list = [1,2,3,4,4,4,5,6,7,8,8,8]
for i in exanmple_list:
    print(i)
    print("inner of for")

print("out")

for i in range(11):  ##1-10
    print(i)

for i in range(1,10):   ##1-9
    print(i)

for i in range(1,10,3): ## 1 4 7
    print(i)

##if条件
x = 1
y = 2
z = 0

if x<y>z:
    print("x<y>z")

##if-else条件
x = 1
y = 2
z = 3

if x>y:
    print("x>y")
else:
    print("x<=y")


##if-elif-else条件
x = -4
y = 2
z = 3

if x>1:
    print("x>1")
elif x<1:
    print("x<1")   ##第一次满足条件就跳出程序 print x<1
elif x < -1:
    print("x< -1")
else:
    print("x=1")


##def 函数
def SSum():
    print("ssssss")
SSum()

##函数 参数
def fun(a,b):
    c = a+b
    print("The is c: {}".format(c))
    print("The is c:",c)
fun(2,5)

##函数默认参数
def sale_car(price,color="red",brand="carmy",is_second_hand=True):
    print("price: {},"
          "color: {},"
          "brand: {},"
          "is_second_hand: {}"
          .format(price,color,brand,is_second_hand))
sale_car(10000)
sale_car(100,"black")


##全局 局部变量  global local
X = 100 ##global
def fun():
    a = 10  ##local
    print(a)
    return a+X
b = fun()
print(b)
print(X)


##模块安装
#numpy pandas 等等 在pycharm中直接安装就行

##读写文件1
text  = "This is my first test.\nThis is next line.\nThis is last line."
print(text)

my_file = open('test.txt','w')
my_file.write(text)
my_file.close()

##读写文件2
append_text = "\nThis is appended file."
my_file = open('test.txt','a')
my_file.write(append_text)
my_file.close()

##读写文件3
file = open('test.txt','r')
content = file.read()
print(content)
#后续的pandas的可以读取excel的文件 csv的文件 后续再讲

##class类
class Calculator:
    name = "Good calculator"
    price = 18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

cal = Calculator()
print(cal.name)
print(cal.price)
cal.add(1,2)
cal.minus(10,11)
cal.times(13,2)

##类 init 功能
class Calculator:
    name = "Good calculator"
    price = 18
    def __init__(self,name,price,hight,width,weitght):
        self.name = name
        self.price = price
        self.hight = hight
        self.width = width
        self.weight = weitght
        self.add(1,3)  #初始化该类时就执行add的功能
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

cal  = Calculator("bad",10,11,22,33)
#print(cal.name)
#print(cal.price)



##input输入
a_input = input("please give a number:")  #return is string
print("This input number is:",a_input)
if a_input == "1":
    print("This is a good one")
elif a_input == "2":
    print("See you next time.")
else:
    print("Good luck.")


##元组 列表
a_tuple = (1,2,3,4,43)
a_list = [1,3,4,2,1]

for i in a_tuple:
    print(i)
for index in range(len(a_tuple)):
    print(a_tuple[index])

for i in a_list:
    print(i)
for index in range(len(a_list)):
    print("index:{}".format(index))
    print(a_list[index])

##列表 list
a = [1,2,3,4,5]
a.append(11)
print(a)
a.insert(1,100) #从0开始
print(a)
a.remove(2) #减少第一次出现的数字
print(a)
print(a[0])
print(a[len(a)-1]==a[-1])
print(a[:3])
print(a[2:4])
print(a[-2:])
print(a.index(100))  #返回第一次出现的索引
print(a.count(100))  #出现的总次数
a.sort() #默认从小到大
a.sort(reverse=True)

##多维列表 numpy pandas 这些会用到
a = [1,2,3,4]
a_multi = [[1,2,3],[2,2,4],[2,5,7]]
print(a_multi[0][1])

##字典 dictionary
a_list = [1,2,3,4,5,6]
d = {'apple':[1,2,3,4],'pear':2,'orange':3}
print(d['apple'])
print(a_list[0])
del d['pear'] #delete
print(d)
d['b'] = 100
print(d)  #无顺序
print(d['apple'][2]) #字典包含字典and list，and so on

##import 载入模块
from time import time,localtime
#from time import *

print(localtime())
print(time())
#print(t.time())


##自己的模块
from mofan.python_base.m1 import printData
aa = printData(22)
print(aa)

##continue and break
a = True
while(a):
    b = input("type:")
    if b=="1":
        a = False
    else:pass

print("run finish")

while(True):
    b = input("type:")
    if b=="1":
        break
    else:pass

print("run finish")

while(True):
    b = input("type:")
    if b=="1":
       continue
    else:pass
    print("still in while")

print("run finish")


##错误处理 try
try:
    file = open('eee.txt', 'r+')
except Exception as e:
    print("There is no file named as eee.")
else:
    file.write('sss')
file.close()

##zip lambda map
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i/2,j*2)


print(list(zip(a,a,b)))

def fun2(x,y):
    return x+y
print(fun2(2,3))

fun3 = lambda x,y:x+y
print(fun3(2,3))


print(list(map(fun2,[1],[2])))
print(list(map(fun2,[1,2],[3,4])))

##copy and deepcopy
import copy
a = [1,2,3]
b = a
print(id(a))
print(id(b))
b[0] = 2
print(a)
print(b)

c = copy.copy(a)
print(id(c)==id(a))

a = [1,2,[3,4]]
d = copy.copy(a)
print(id(d)==id(a))
print(id(d[2])==id(a[2]))  #True

e = copy.deepcopy(a)
print(id(e[2])==id(a[2]))  #False


##tkinter 窗口 ---GUI界面

##pickle存放数据
import pickle
a_dict = {"da":11,2:[2,3,4],"23":{1:2,"d":"sad"}}
file = open("pickle.pickle",'wb')
pickle.dump(a_dict,file)
file.close()


file1 = open("pickle.pickle","rb")
a_dict1 = pickle.load(file1)
print(a_dict1)

##set找不同
char_list = ['a','a','b','b','c','c','c']
sentence = 'Welcome Back to my home'
print(set(char_list))
print(type(set(char_list)))
print(set(sentence))

unique_char = set(char_list)
unique_char.add('x')  #add
print(unique_char)
#unique_char.clear()
#print(unique_char)
unique_char.remove('x')  #unique.discard('y') #若没有y，则返回原序列，不报错
print(unique_char)

set1 = unique_char
set2 = {"a","e","r"}
print(set1.difference(set2))
print(set1.intersection(set2))

##正则表达式##  爬虫
import re

####简单的匹配
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)
print(pattern2 in string)

####使用正则寻找配对
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1,string))
print(re.search(pattern2,string))

###匹配多种可能
ptn = r"r[au]n"
print(re.search(ptn,"dog runs to cat"))
print(re.search(r"r[A-Z]n","dog runs to cat"))
print(re.search(r"r[a-z]n","dog runs to cat"))
print(re.search(r"r[0-9]n","dog r2ns to cat"))
print(re.search(r"r[0-9A-Z]n","dog runs to cat"))

##特殊种类的匹配
###\d decimal digit
print(re.search(r"r\dn","run r4n"))
####\D any non-decimal digit
print(re.search(r"r\Dn","run r4n"))

##空白
###\s any white space [\t\n\t\f\v]
###\s oppoite to \s ,any non-white space
print(re.search(r"r\sn","r\nn r4n"))
print(re.search(r"r\Sn","r\nn r4n"))

##所有字母数字和“_”
###\w [a-zA-Z0-9_]
###\W opposite to \w
print(re.search(r"r\wn","r\nn r4n"))
print(re.search(r"r\Wn","r\nn r4n"))

###空白字符
#\b empty string (only at the start or end of the word)
#\B empty string (BUt not at the start or end of the word)
print(re.search(r"\bruns\b","dog runs to cat"))
print(re.search(r"\B runs \B","dog  runs  to cat"))

##特殊字符
#\\ match \
#. match anything (except \n)
print(re.search(r"runs\\","runs\ to me"))
print(re.search(r"r.n","r[ns to me"))

##句首句尾
# ^ match line beginning
# $ match line ending
print(re.search(r"^dog","dog runs to cat"))
print(re.search(r"cat$","dog runs to cat"))

##是否
# ? may or may not occur
print(re.search(r"Mon(day)?","Monday"))
print(re.search(r"Mon(day)?","Mon"))

##多行匹配
string  = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I",string))   #None
print(re.search(r"^I",string,flags=re.M)) #<re.Match object; span=(18, 19), match='I'>

###0或多次
# *  occur 0 or more times
print(re.search(r"ab*","a"))
print(re.search(r"ab*","abbbbbbb"))

###一次或多次
#  +   occur 1 or more times
print(re.search(r"ab+","a"))  #None
print(re.search(r"ab+","abbbbbbb"))

### 可选次数
#{n,m} : occur n to m  times
print(re.search(r"ab{2,10}","a")) #None
print(re.search(r"ab{2,10}","abbbbbbb"))


###group组
match = re.search(r"(\d+), Date: (.+)","ID: 021523, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))

match1 = re.search(r"(?P<id>\d+), Date: (?P<date>.+)","ID: 021523, Date: Feb/12/2017")
print(match1.group('id'))
print(match1.group('date'))

###寻找所有匹配
print(re.findall(r"r[ua]n","run ran ren"))
print(re.findall(r"(run|ran)","run ran ren"))

##替换
print(re.sub(r"r[au]ns","catches","dog runs to cat"))

##分裂
print(re.split(r"[,;\.]","a;b,c.d;e"))  #['a', 'b', 'c', 'd', 'e']

#compile
compile_re = re.compile(r"r[ua]n")
print(compile_re.search("dog ran to cat"))




'''
map:把什么功能附加给一个他的参数，也就是说map分两部分，一个是功能一个是参数
    把他们俩合起来的一个运算
lambda：就相当于map的功能，一个简化的功能（函数）
zip:为迭代器所做的一个简单的工具
'''



#【zip】
'''
a=[1,2,3]
b=[4,5,6]

zip(a,b)#返回的值是一个对象（object）,想可视化需要将其变成一个list
print(list(zip(a,b)))#迭代合并

#想每一步同时输出a的第一位和b的第一步
for i,j in zip(a,b):
   print(i/2,j*2)


#zip多个元素
print(list(zip(a,a,b)))
'''

#【lambda】

def fun1(x,y):
    return(x+y)
'''
fun2=lambda x,y:x+y #lambda实现,这种简单的方程只需一行代码
'''

#【map】已知的功能加上所给的参数一起输进去运算
map(fun1,[1],[2]) #参数用列表的形式输入，表示x=1,y=2，这样输出返回值是object
r=list(map(fun1,[1],[2]))
print(r)

#可以输入更多的参数
r=list(map(fun1,[1,3],[2,5]))#x=1加上y=2,x=3加上y=5
print(r)





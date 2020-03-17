#tuple list

#a_tuple=(12,2,3,4,5,623)
#another_tuple=2,3,43,5,

#a_list=[12,3,6,7,9]

#for index in range(len(a_tuple)):
#    print('index=',index,'number in list=',a_tuple[index])



a=[1,2,3,4,62,5,6]
#a.append(0) 在列表后追加值
#print(a)

#a.insert(1,0)  参数1表位置（列表下标从0开始），参数2表插入的值

#a.remove(2) #括号内是去掉的值，而非位置；去掉第一个出现的2

print(a)

print(a[1])

print(a[-1]) #打印最后一位数

print(a[3:5])#打印一串值
print(a[-3:]) #打印一串值 从倒数第三个开始往后数[62,5,6]

print(a.index(2))#列表中第一次出现2的索引

print(a.count(4))#列表中出现4的次数

a.sort() #对列表从小到大进行排序，结果会覆盖掉原来的列表
print(a)

a.sort(reverse=True) #对列表从大到小进行排序
print(a)


#多维数组
multi_dim_a=[[1,2,3],
            [2,3,4],
            [3,4,5]]
print(multi_dim_a[0][1])

#要获取矩阵的更多信息需要 import numpy




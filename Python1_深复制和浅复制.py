import copy


a=[1,2,3]
b=a #a,b的索引在计算机的同一块区域，只是用不同的变量表示

#用id()来查看索引
print(id(a))
print(id(b)) #a,b的id完全一样

b[0]=11
print(a) #改变b，a也同时被改变

#【浅复制shallowcopy】
c=copy.copy(a)
print(id(a)==id(c)) #结果为False,a和c不再是同一个东西

c[1]=000
print(a) #改变c，a不变


a=[1,2,[3,5]]
d=copy.copy(a)
print(id(a)==id(d)) #结果为False
print(id(a[2])==id(d[2])) #结果为True

a[0]=[11]
print(d) #改变a[0],a[1],d不变

a[2][0]=333
print(d) #改变a[2],d被改变
#当列表中还有列表时，copy.copy()只会复制最外层，里层的列表id不会改变
#以上为copy.copy()的独特功能（浅复制）

#希望完完全全复制，id不会有任何重复
#【深复制 deepcopy】
e=copy.deepcopy(a)
print(id(e[2])==id(a[2]))



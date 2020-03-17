#当你想要在列表或元组中找到一些不同之处，set会剔除掉所有重复内容，只留下不一样的
char_list=['a','b','c','c','d','d','d']
#print(set(char_list)) #剔除重复元素，返回结果是乱序的
#print(type(set(char_list))) #类型是set（用{}括起来的，但不是字典）

sentence='Welcome Back to This Tutorial' 
#print(set(sentence)) #空格也会当成元素留下来，大小写当成不重复的元素

#将char_list和sentence一起set会报错，所以set里 不能传列表加列表的形式

#【set的一些功能】
unique_char=set(char_list)

unique_char.add('x') #加一个元素,与原来的set元素重复的元素不会被添加进去
#不可以加入一组数（一个list）,unique_char.add(['x','y'])会报错

#unique_char.clear() #清空set

'''
unique_char.remove('x') 
print(unique_char.remove('x')) #该语句的返回值是none，返回的是减掉的内容
print(unique_char)
'''

unique_char.discard('y') #remove减去不存在的元素会报错，discard不会报错，会返回原内容
#print(unique_char)


#对两个set找不同
set1=unique_char
set2={'a','e','i'}
print(set1.difference(set2)) #返回两个set不同的元素所组成的set
print(set1.intersection(set2)) #返回两个set的交集


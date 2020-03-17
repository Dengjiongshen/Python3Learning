#列表是有顺序的，字典是无序的

a_list=[1,2,5,6,7,9] #列表用中括号

d={'apple':1,'pear':2,'orange':3} #字典用大括号，每一个key对应一个value

d2={1:'a','c':'b'}

#print(d['apple']) 打印key=apple的元素的value
#print(a_list[0])

del d['pear'] #删除元素

d['b']=20 #插入元素，无序

d3={'apple':[1,2,3],'pear':{1:3,3:'lala'}} #字典里面是列表和字典


print(d3['pear'][3]) #打印key=pear的元素里key=3的元素的value



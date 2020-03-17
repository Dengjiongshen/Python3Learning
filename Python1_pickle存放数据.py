import pickle
#pickle模块可以帮助在你想要保存Python运算完的结果，之后隔几天想提取再继续加工
a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'kak'}}

#file=open('pickle_example.pickle','wb') #'wb'以二进制的形式写入
#pickle.dump(a_dict,file) #将字典a_dict装入文件file
#file.close()

#【假设隔了一天想要打开文件继续加工】
file=open('pickle_example.pickle','rb')
a_dict1=pickle.load(file)
file.close()
print(a_dict1)

#简单一点的做法，在运行后自动关闭文件，不用担心会忘记关文件
with open('pickle_example.pickle','rb') as file: #将之前文件装载到file里
    a_dict1=pickle.load(file) #pickle读取

#写入也可以用with简写

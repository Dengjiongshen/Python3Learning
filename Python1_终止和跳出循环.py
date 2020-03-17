#终止循环和跳过循环

'''
a=True
while a:
    b=input('type something') #input获得的是字符串
    if b=='1': #后面的语句还会执行才会退出循环
        a=False
    else:
        pass
'''

'''
while True:
    b=input('Type something:')
    if b=='1':
        break #跳出循环
    else:
        pass
    print('still in while')
print('finish run')
'''


while True:
    b=input('Type something:')
    if b=='1':
        continue #跳过continue后的所有语句，再进入下一个while循环
    else:
        pass
    print('still in while')
print('finish run')

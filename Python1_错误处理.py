try:
    file=open('eee','r+')
except Exception as e:#将异常信息存储在e里
    print(e)
    print('there is no file named as eee')
    response= input('do you want to create a new file?')
    if response=='y':
        file=open('eee','w')
    else:
        pass
else:#有错误执行exception语句，没有错误执行else语句
    file.write('sss')
file.close()
    

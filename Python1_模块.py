#【如何import一个官方/外部模块，内部下载好的模块】
#import time #import载入模块（方法一）
#import time as t #当模块名很长时（方法二）
print(time.localtime())

from time import time,localtime #只想要time,localtime这两个功能（方法三）
print(localtime()) #此时直接调用前面不能加模块名
print(time())

from time import * #导入所有功能（方法四）
print(localtime()) #此时直接调用前面不用加模块名
print(gettime())




#【如何导入自己的模块（自己创建好的脚本）】
#想在P1.py里import my.py
#只要确保自己所创建的P1和my在同一个目录下，就可以import my
#当把自己创建的my拉到site-packages文件夹下（相当于从网上下载下来安装到Pyhon默认的外部模块链接里）
#此时，就不用必须非要和P1再同一个目录下才能调用，可直接调用


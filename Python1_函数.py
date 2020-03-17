class Calculator:
    name='good'
    price=10
    def __init__(self,name,price,hight):#init前后是双下划线
        self.name=name
        self.price=price
        self.hight=hight
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        result=x*y
        print(result)
    def divide(self,x,y):
        result=x/y
        print(result)
    

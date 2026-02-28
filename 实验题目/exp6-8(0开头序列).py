def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        n=f(n-1)+f(n-2)
        return n
n=int(input())
a=[f(i)for i in range(n)]
print(a)
sf=sum(a)
print(sf)
'''print([i for i in range(10)])
   [0,1,2,3,4,5,6,7,8,9]        '''

'''F(n)=F(n-1)+F(n-2)
在 Python 中，函数的返回值是通过 return 语句来实现的，
而不是通过给函数名赋值来实现的。
函数的定义和调用是通过函数名来完成的，
但函数的结果是通过 return 语句返回给调用者的。
函数名本身不是一个可变的容器，不能像变量那样直接赋值。
如果你尝试这样赋值，Python 解释器会认为你正在尝试给一个函数名赋值，
这是不合法的操作。Python 中的函数是不可变的，
它们的值由函数体内的代码逻辑来计算并通过 return 语句返回，
而不是直接赋值给函数名'''
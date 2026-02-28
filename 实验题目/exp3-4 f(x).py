x=float(input("请输入x数值:"))
if x<0:
    print("f(x)=",eval("0-2*x"))
if 0<=x<10:
    print("f(x)=",eval("2*x-1"))
if x>=10:
    print("f(x)=",eval("x*x*x"))
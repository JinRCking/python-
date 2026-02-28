MONTH=float(input("请输入要存入月份:"))
if 0<=MONTH<3:
    print(eval("20000*0.3/100/12*MONTH"))
elif 3<=MONTH<6:
    print(eval("20000*1.4/100/12*MONTH"))
elif 6<MONTH<=12:
    print(eval("20000*1.65/100/12*MONTH"))
elif 12<MONTH<=24:
    print(eval("20000*1.95/100/12*MONTH"))
elif 24<MONTH<=36:
    print(eval("20000*2.4/100/12*MONTH"))
elif 36<MONTH<=60:
    print(eval("20000*2.8/100/12*MONTH"))
elif MONTH>60:
    print(eval("20000*2.8/100/12*MONTH"))
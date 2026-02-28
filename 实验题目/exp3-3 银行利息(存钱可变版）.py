MONEY=float(input("请输入要存的钱:"))
MONTH=float(input("请输入要存入月份:"))
if 0<=MONTH<3:
    print(eval("MONEY*0.3/100/12*MONTH"))
elif 3<=MONTH<6:
    print(eval("MONEY*1.4/100/12*MONTH"))
elif 6<MONTH<=12:
    print(eval("MONEY*1.65/100/12*MONTH"))
elif 12<MONTH<=24:
    print(eval("MONEY*1.95/100/12*MONTH"))
elif 24<MONTH<=36:
    print(eval("MONEY*2.4/100/12*MONTH"))
elif 36<MONTH<=60:
    print(eval("MONEY*2.8/100/12*MONTH"))
elif MONTH>60:
    print(eval("MONEY*2.8/100/12*MONTH"))
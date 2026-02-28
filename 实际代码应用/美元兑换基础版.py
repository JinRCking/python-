def get_rate():
    return 7.1999
rmb=input("输入人民币:")
rate=get_rate()
usd=(eval(rmb))/rate
print("美元为:{:2f}美元".format(usd))
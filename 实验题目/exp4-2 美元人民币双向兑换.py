money=input("请输入金钱值:")
while money[-1]not in['N','n']:
    if money[-3:]in['USD','usd']:
        rmb=(eval(money[0:-3]))/7.1967
        print("转换后的人民币为%.2f人民币"%rmb)
        #print("转化后的人民币为:{:.2f}".format(rmb),"rmb")
    elif money[-3:]in['CNY','cny','RMB','rmb']:
        usd=(eval(money[0:-3]))*7.1967
        print("转换后的美元为%.2fusd"%usd)
    else:
        print("输入格式错误")
    money=input("请输入金钱值:")
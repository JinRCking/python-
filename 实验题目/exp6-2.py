def m(q):
    if q[-3:]in['rmb','RMB']:
        a=(float(q[:-3]))/7.1967
        print("转化后的金额为:%.2fusd"%a)
    if q[-3:]in['usd','USD']:
        b=(float(q[:-3]))*7.1967
        print("转化后的金额为:%.2frmb"%b)
    else:
        print("former false")
q=input("请输入带符号的金额:")
m(q)
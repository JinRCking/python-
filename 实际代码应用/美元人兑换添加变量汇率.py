def get_rate():
    return 7.1999
def usd_to_rmb(usd):
    rmb = usd * rate
    return round(rmb, 2)
rate = get_rate()
usd = float(input("请输入美元金额："))
rmb = usd_to_rmb(usd)
print("转换后的人民币金额为：", rmb)
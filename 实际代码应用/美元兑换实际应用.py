import requests

def get_exchange_rate(api_key):
    url = f"https://v6.exchangeratesapi.io/latest?base=USD&access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"]["CNY"]
    return exchange_rate

def usd_to_rmb(usd_amount, exchange_rate):
    rmb_amount = usd_amount * exchange_rate
    return round(rmb_amount, 2)

# 替换YOUR_API_KEY为你的ExchangeRate-API密钥
api_key = "2c31f2093b8bc779ebf8d666"
# 获取当前汇率
exchange_rate = get_exchange_rate(api_key)

usd_amount = float(input("请输入美元金额："))
rmb_amount = usd_to_rmb(usd_amount, exchange_rate)
print("转换后的人民币金额为：", rmb_amount)

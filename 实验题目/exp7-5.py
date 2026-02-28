import random
red = random.sample(range(1, 34), 6)
red.sort()  # 对红色球号码排序

    # 生成1个蓝色球号码，从1到16中选择
blue = random.randint(1, 16)

    # 将红色球号码转换为字符串并用'-'连接
red_str = '-'.join(map(str, red))
blue_str = str(blue)

    # 拼接最终的双色球号码
print( f"福彩双色球号码: {red_str}-{blue_str}")
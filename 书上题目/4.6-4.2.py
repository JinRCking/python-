# 从键盘获取输入
line = input("请输入一行代码：")

# 初始化统计变量
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 遍历输入的每个字符并统计
for A in line:
    if A.isalpha():  # 判断是否为字母
        letter_count += 1
    elif A.isdigit():  # 判断是否为数字
        digit_count += 1
    elif A.isspace():  # 判断是否为空格
        space_count += 1
    else:
        other_count += 1  # 其他情况视为其他字符

# 输出统计结果
print("英文字符个数：", letter_count)
print("数字个数：", digit_count)
print("空格个数：", space_count)
print("其他字符个数：", other_count)

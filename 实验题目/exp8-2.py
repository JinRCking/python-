# 打开输入和输出文件
fr = open("price2016.csv", "r", encoding="utf-8")
fw = open("price2016out.csv", "w", encoding="utf-8")

# 用于存储从输入文件读取的数据的列表
ls = []

# 将CSV文件中的二维数据读入到列表变量
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(","))

# 遍历列表变量计算百分数
for i in range(1, len(ls)):  # 从1开始以跳过标题行
    for j in range(1, len(ls[i])):  # 从1开始以跳过城市名称
        ls[i][j] = str(float(ls[i][j]) / 100) + "%"  # 转换为百分数并添加%

# 将列表变量中的二维数据输出到CSV文件
for row in ls:
    fw.write(",".join(row) + "\n")

# 关闭文件
fr.close()
fw.close()

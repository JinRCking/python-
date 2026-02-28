import os
 # 定义要写入的内容
a="Hello Python!"
 # D盘根目录的路径（Windows环境）
b="D:\\"
 # 文件路径
c=os.path.join(b, "1.txt")
 # 写入文件
with open(c, 'w', encoding='utf-8') as A:
A.write(a)
 # 确保数据已写入并关闭文件
A.close()
 # 输出写入后文件的内容
with open(c, 'r', encoding='utf-8') as B:
C = B.read()
print(f"文件内容：{C}")
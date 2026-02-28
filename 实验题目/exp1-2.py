import math
radius = input("请输入圆的半径")
radius = float(radius)
area=math.pi*radius*radius
print("若圆的半径为{:.2f}厘米".format(radius))
print("则该圆的面积为{:.2f}平方厘米".format(area))
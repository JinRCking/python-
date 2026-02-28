G=eval(input("请输入毕设成绩"))
if 85<G<=100:
    print("优秀")
elif 75<G<=84.9:
    print("良好")
elif 66<G<=74.9:
    print("中等")
elif 60<G<=65.9:
    print("及格")
elif 0.0<G<=59.9:
    print("不及格")
else:
    print("输入错误")
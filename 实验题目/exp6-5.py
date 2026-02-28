def f(q):
    a=b=c=d=0
    for i in q:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    print("英文字符个数：", a,"数字个数：", b,"空格个数：", c,"其他字符个数：", d)
    
    
    
q=input("请输入")
f(q)
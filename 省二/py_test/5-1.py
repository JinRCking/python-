#请在下面位置编写程序
a=[]
for i in range (0,9):
    a.append(0)
    a.append(1)
    if i>=2:
        a[i]=a[i-1]+a[i-2]
        a.append(a[i])
q=sum(a)
print(q)

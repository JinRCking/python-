ls=[]
s=0
for i in range(10,100):
    A=int(str(i)[0])
    B=int(str(i)[1])
    
    if A*B>A+B:
        s=s+1
        ls.append(i)
print(s)
print(ls)
S=[]
T=[]
for i in range(len(s)):
    if t[i]==0:
        S.append(s[i])
    elif t[i]==1:
        T.append(s[i])
SS=sum(S)/len(S)
TT=sum(T)/len(T)
result=SS-TT

if result<0:
    real_result=-result
    print(real_result)
else:
    real_result=result
    print(real_result)
#结束
save(real_result)
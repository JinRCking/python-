a=[]
for i in range(len(s)):
    if t[i]>=85:
        e=s[i]+t[i]
        a.append(e)

A=sorted(a)
result=A[-30]
print(result)
save(result)

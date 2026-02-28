S=[]
T=[]
Q=[]
for i in range(len(t)):
    if t[i]>=85:
        S.append(s[i])
        T.append(t[i])
for j in range(len(S)):
        e=S[j]+T[j]
        Q.append(e)
        sorted(Q)
print(Q[-30])
save(Q)

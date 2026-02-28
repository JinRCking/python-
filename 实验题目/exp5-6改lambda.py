f=lambda x:1/sum(range(1,x+1))
S = sum(map((f), range(1, 11)))
print(S)



print(sum(map(lambda x:1/sum(range(1,1+x)),range(1,11))))
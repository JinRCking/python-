n=0
for i in range(500,2001):
    if i%7==0 and int(str(i)[-1])==2:
        n=n+1
        print(i)
print('一共',n,'个')
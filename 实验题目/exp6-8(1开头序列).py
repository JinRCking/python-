def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        n=f(n-1)+f(n-2)
        return n
n=int(input())
a=[f(i)for i in range(1,n+1)]
print(a)
sf=sum(a)
print(sf)
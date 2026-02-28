def f(q):
    if int(q[5:7])==12 and 21<int(q[8:10])<=31 or int(q[5:7])==1 and 0<int(q[8:10])<=19:
        print("摩羯座")
    else:
        print()
q=input()
f(q)
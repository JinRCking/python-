def taxRate(income):
    point=5000
    a=income-point
    if a<=0:
        rate=0
        b=0
    elif a<=3000:
        rate=0.03
        b=a*rate-0
    elif a<=12000:
        rate=0.10
        b=a*rate-210
    elif a<=25000:
        rate=0.20
        b=a*rate-1410
    elif a<=35000:
        rate=0.25
        b=a*rate-2660
    elif a<=55000:
        rate=0.30
        b=a*rate-4410
    elif a<=80000:
        rate=0.35
        b=a*rate-7160
    else:
        rate=0.45
        b=a*rate-15160
    print(rate)
    print(b)

x=float(input())
taxRate(x)

for n in range(100,1000):
    A=float(str(n)[0])
    B=float(str(n)[1])
    C=float(str(n)[2])
    if n==A**3+B**3+C**3:
        print(n)
for A in range(1,1001):
    
    C=0
    for B in range(1,A//2+1):
        if A%B==0:
            C=C+B
            
    if C==A:
        print(A)
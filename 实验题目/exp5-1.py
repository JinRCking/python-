A=B=0
for i in range(9, 0, -1):
    B = B * 10 + i
    A += B
    print('B=',B)
    print('A=',A)
print('s=',A)
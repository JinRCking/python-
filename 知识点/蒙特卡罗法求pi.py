from random import random
from math import sqrt
from time import time
DARTS=500000000
hits=0.0
start_time=time()
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
end_time=time()
print("pi  is:{}".format(pi))
print("tim is:{:.5f}s".format(end_time-start_time))
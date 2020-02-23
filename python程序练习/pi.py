from random import random
from math import sqrt
from time import clock
a=pow(2,25)
b=0
clock()
for i in range(1,a):
    x,y=random(),random()
    d=sqrt(x**2+y**2)
    if d<=1.0:
        b=b+1
pi=4*(b/a)
print("Pi的值是 %s" % pi)
print("运行时间 %-5.5ss" % clock())

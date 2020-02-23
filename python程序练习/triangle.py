import math
def square(x):
    return x*x
12
def dist(x1,y1,x2,y2):
    dist=math.sqrt(square(x1-x2)+square(y1-y2))
    return dist

def istriangle(x1,y1,x2,y2,x3,y3):
    flag=(((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2))!=0)
    return flag

def main():
    x1,y1=eval(input('点1,x1,y1='))
    x2,y2=eval(input('点2,x2,y2='))
    x3,y3=eval(input('点3,x3,y3='))
    if istriangle(x1,y1,x2,y2,x3,y3):
        C=dist(x1,y1,x2,y2)+dist(x1,y1,x3,y3)+dist(x2,y2,x3,y3)
        print('该三角形周长为:',C)
    else:
        print('This is not a triangle !')
main()

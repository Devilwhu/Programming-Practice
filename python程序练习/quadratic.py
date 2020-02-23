import math
def main():
    a,b,c=eval(input('请输入二次方程系数a,b,c\n'))
    d=b*b-4*a*c
    if a==0:
        root=-c/b
        print('根为：',root)
    elif d==0:
        root=-b/(2*a)
        print('根为：',root)
    elif d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print('\n该方程根为:',root1,root2)
    else:
        print('没有实根！')
main()
    

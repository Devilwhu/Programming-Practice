def main():
    n=eval(input('请输入共有多少个数？\n'))
    max=eval(input('输入一个数:'))
    for i in range(n-1):
        x=eval(input('输入一个数:'))
        if x>max:
            max=x
    print('最大数为:',max)
main()

        

for n in range(2,1000):
    for i in range(2,n):
        if n%i==0:
            print(n,'equals',i,'*',n//i)
            break
    else:
        print(n,'is a prime number')

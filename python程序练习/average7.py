def main():
    filename=input('What file are the numbers in?')
    infile=open(filename,'r')
    sum=0
    count=0
    line=infile.readline()
    while line!='':
        for xstr in line.split(','):
            sum=sum+eval(xstr)
            count=count+1
            line=infile.readline()
    print('\nThe average of the numbers is',sum/count)
main()
        

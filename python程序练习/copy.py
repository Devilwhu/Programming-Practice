def copy():
    f1=input('enter a source file:').strip()
    f2=input('enter a source file:').strip()

    infile=open(f1,'r')
    outfile=open(f2,'w')

    countlines=countchars=0
    for line in infile:
        countlines += 1
        countchars += len(line)
        outfile.write(line)
    print(countline,'lines and ',countchars,'chars are copied')

    infile.close()
    outfile.close()
copy()

        
        
        

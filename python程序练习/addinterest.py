def addinterest(balance,rate):
   balance=balance*(1+rate)
   return balance
    #for i in range(len(balance)):
       #balance[i]=balance[i]*(1+rate)
def main():
    amounts=1000
    #amounts=[1000,750,500,250]
    rate=0.05
    amounts=addinterest(amounts,rate)
    print(amounts)
main()

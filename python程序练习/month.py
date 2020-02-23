months='JanFebMarAprMayJunJulAugSepOctNovDec'
n=input('请输入月份数字')
pos=(int(n)-1)*3
print('月份简写为'+months[pos:pos+3]+'.')

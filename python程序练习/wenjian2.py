def main():
#打开文件，读取文件
    file1=open('C:\\Users\Devil\Desktop\python学习\Chapter 6\字典实例二数据\EmailAddressBook.txt','rb')
    file2=open('C:\\Users\Devil\Desktop\python学习\Chapter 6\字典实例二数据\TeleAddressBook.txt','rb')

    file1.readline()
    file2.readline()
    line1=file1.readlines()
    line2=file2.readlines()

#建立空列表用于存储姓名、电话、邮箱
    list1_name=[]
    list1_tele=[]
    list2_name=[]
    list2_email=[]

#获取两个book中的信息
    for line in line1:
        elements=line.split()
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))

    for line in line2:
        elements=line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))

    lines=[]
    lines.append('姓名\t  电话\t    邮箱\n')

    for i in range(len(list1_name)):
        s=''
        if list1_name[i] in list2_name:
            j=list2_name.index(list1_name[i])
            s='\t'.join([list1_name[i],list1_tele[i],list2_email[i]])
            s+='\n'
        else:
            s='\t'.join([list1_name[i],list1_tele[i],str('------')])
            s+='\n'
        lines.append(s)

    for i in range(len(list2_name)):
        s=''
        if list2_name[i] not in list1_name:
            s='\t'.join([list1_name[i],str('------'),list2_email[i]])
            s+='\n'
        lines.append(s)

    file3=open('C:\\Users\Devil\Desktop\python学习\Chapter 6\字典实例二数据\AddressBook.txt','w')
    file3.writelines(lines)
    file1.close()
    file2.close()
    file3.close()
if _name_=='_main_':
    main()


        

        
        


    
    


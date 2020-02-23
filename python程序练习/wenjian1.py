from turtle import Turtle,mainloop
def main():
    #设置窗口信息和turtle画笔
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)

    pen=turtle.Turtle()
    pen.color('red')
    pen.width(5)
    #pen.shape('turtle')
    pen.speed(5)
    
    #读取数据文件到列表result中
    result=[]
    file=open('C:\\Users\Devil\Desktop\python学习\Chapter 6\文件实例一数据\data.txt','r')
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)

    #根据每一条数据进行绘制
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.forward(result[i][0])

        if result[i][1]:
            pen.right(result[i][2])
        else:
            pen.left(result[i][2])
    pen_goto(0,0)
if _name_ == '_main_':
    main()
        
        
    
        

    
    

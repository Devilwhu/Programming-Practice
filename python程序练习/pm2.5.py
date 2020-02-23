def main():
   PM=eval(input('请输入PM2.5指数\n'))
   if PM>75:
       print('空气污染警告！')
   if PM<35:
       print('空气质量良好，建议户外运动！')
main()

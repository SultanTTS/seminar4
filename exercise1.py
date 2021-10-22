try:
     a=int(input("Первое число="))
     b=int(input("Второе число="))
     c=int(input("Третье число="))
     d=int(input("Четвертое число="))
except:
     print("Только число!")
     exit()
def exe1(num1, num2, num3, num4):
       if (num1>5) and (num2>5) and (num3%6==0) and (num4 % 3!= 0) :
             print("yes")
       else:
             print("no")
exe1(a, b ,c, d)

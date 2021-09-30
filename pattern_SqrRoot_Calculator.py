from math import sqrt
num=int(input("Enter 0 to 9 number for printing star pattern and  Enter greater of 10 for sqere root :"))
if num<=10:
   for i in range(num):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
else:           
  sqrt1=sqrt(num)
  print(sqrt1)

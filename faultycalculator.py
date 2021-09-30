print("Enter a number: ")
num1=int(input())
print("Enter second number:")
num2=int(input())
print("Enter a operator what do you want to:"+"+","-","*","/","%")
num3=input()
if num1==400 and num2==500 and num3=='+':
    print("777")
elif num1==20 and num2==5 and num3=='*':
        print("70")
elif num1==200 and num2==100 and num3=='-':
            print("500")
elif num1==50 and num2==2 and num3=='/':
    print("20")
elif num3=='+':
    num4=num1+num2
    print(num4)
elif num3=='-':
    num4=num1-num2
    print(num4)
elif num3=='*':
    num4=num1*num2
    print(num4)
elif num3=='/':
    num4=num1+num2
    print(num4)
elif num3=='%':
    num4=num1%num2
    print(num4)
else:
    print("invalid number plesase enter a vald number: ")
                                
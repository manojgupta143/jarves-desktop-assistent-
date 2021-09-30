from math import sqrt
print("Welcome to math and numric conversion calculator :")
print(""" if you want to convert any base Number into Any other base please use these code "Before"Entering the Number
    For Binary use:                  0b "for example 0b1111"   
    For Ocat Number use:             0o "for example 0o245"
    For Hexa decimal Number use:     0x "for example 0xface"
    For Decimal Number use:          "for example 0b1111" """)
b="b"
h="h"
o="o"
no=1
decimal=eval(input("Enter Number with code for conversion :"))
print("Enter 'b'for binary 'h' for hexa decimal number and 'o' for octal :")
num=eval(input("please Enter your input :"))
if num==b:
    binary=bin(decimal)
    print(binary)
elif num==o:
    octal=oct(decimal)
    print(octal)
elif num==h:
    hexa=hex(decimal)
    print(hexa)
elif num==1:
    num2=int(decimal)
    print(num2)
else:
    print("Provaided Number is invalid plese provaid valid number with hiscode the code is for hexa 0x for octal 0o for binary 0b")

num=int(input("Enter a Number :"))
for a in range(1,num+1,2):
    for i in range(1,num+1):
        print(" "*(2*num-i-a))

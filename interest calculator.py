no=1
op=int(input("press 1 for compound interest 0 for simple interest :"))
if op==True:
    Pamount=int(input("Enter  your interest amount :"))
    rate=float(input("Enter Your interest rate :"))
    tym=int(input("Enter your time month/Year :"))
    total=Pamount*rate/100+Pamount
    print(f"Your First years Amount is {total}")
    def interest(amount,rate,tym):
        amount=total*rate/100+total
        return amount
    total=interest(total,rate,tym)
    print(f"Second Month interest is {total}")
    for i in range(2,tym):
        total=total*rate/100+total
        print(f"Your {i} Interest Is {total}")
elif op==False:
    amount=int(input("Enter  your interest amount :"))
    rate=float(input("Enter Your interest rate :"))
    tym=int(input("Enter your time month/Year :"))
    simple_interest=amount*rate/100*tym
    print(f"This is your simple interest {simple_interest}")
    print(f"This is your interest amount {simple_interest+amount} for {tym} month")
else:
    print("invalid input")
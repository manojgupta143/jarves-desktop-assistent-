import sys
class Costmers:
    bankName="Central Bank Of India"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("your amaount Is ",self.balance)
    def withdrow(self,amt):
        if amt>self.balance:
            print("You Dont Have sufficient Balance Please Try Again")
            sys.exit()
        else:
            self.balance=self.balance-amt
            print("Your Amount Is ",self.balance)
print("welcome To",Costmers.bankName)
name=input("Enter Your Name :")
c=Costmers(name)
while True:
    print("Do You want To Withdrow Or Deposit , press W- for Withdorow And D- For Deposit E- For Exit :" )
    option=input("choose Your Option :")
    if option.lower()=="d":
        amt=float(input("Enter Your Amaount How Much Do You Want To Diposit :"))
        c.deposit(amt)
        print("your amount deposit succesfully ")
    elif option .lower() =="w":
        amt=float(input("Enter Your Amount :"))
        c.withdrow(amt)
        print("your withdrowal seccessful")

    elif option.lower()=="e":
        sys.exit()
    else:
        print("Please Choose Valid Option")
    

        

        


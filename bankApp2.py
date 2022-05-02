import datetime
import sys
time=float(datetime.datetime.now().hour)
class Account:
    bank="Central Bank Of India "
    def __init__(self,name,accountNo,balance,min_balance):
        self.name=name
        self.accountNo=accountNo
        self.balance=balance
        self.min_balance=min_balance
    def deposit(self,amount):
        self.balance =self.balance=amount
        print("YOur Current Balance Is ",self.balance)
    def withdrow(self,amount):
        if self.balance -amount>=self.min_balance:
            self.balance-amount
        else:
            print("You Do Not Have A suffucuent Balance ")
    def statement(self):
        print("Name Of The Costmer Is ",self.name)
        print("account  Number Of The Costmer Is ",self.accountNo)
        print("Balance Of The Costmer Is ",self.balance)
        print("Your Time Of Transaction Of",time)
class SavingAccount(Account):
    def __init__(self, name, accountNo, balance ):
        super().__init__(name,accountNo, balance,0)
    def __str__(self):
        return "It is {}'s saving account with {}".format(self.name,self.balance)
class CurrentAccount(Account):
    def __init__(self, name, accountNo, balance, ):
        super().__init__(name,accountNo, balance,-10000)
    def __str__(self):
        return "It is {}'s Current account with {}".format(self.name,self.balance)
print("Welcome To ",Account.bank)
print()
n=int(input("Enter The Number Of Costmers :"))
for i in range(n):
    name=input("Enter Costmer Name :")
    accNo=(input("Enter Costmer Account no :"))
    Blns=(input("Enter Your Amount :"))
    s=SavingAccount(name,accNo,Blns)
    

option=input("Enter Your Account Type :[saving | Current] :")
if option.lower()== "saving":
    varification=input("Enter Your Account No :")
    if varification== s.accountNo:
        print("Do You Want To Deposit Or Withdrow")
        option2=input("Enter D- For Deposit W- for withdrow E-For Exit :")

        if option2 == "D"or "d":
                amt= float(input("Enter Your Amount :"))
                s.deposit(amt)
                s.statement()
        elif option2 == "W"or "w":
            amt= float(input("Enter Your Amount :"))
            s.withdrow(amt)
            s.statement()
        elif option2=="E"or "e":
            sys.exit()
        else:
            print("Thanks For Using Application ")
    else:
        print("Your Account No Is Not valid ")
        sys.exit()
if option.lower()== "current":
    c=CurrentAccount(name,accNo,Blns)
    varification=input("Enter Your Account No :")
    if varification== c.accountNo:
        
       print("Do You Want To Deposit Or Withdrow")
       option2=input("Enter D- For Deposit W- for withdrow E-For Exit :")
       if option2 == "D"or "d":
          amt= float(input("Enter Your Amount :"))
          c.deposit(amt)
          c.statement()
    elif option2 == "W"or "w":
        amt= float(input("Enter Your Amount :"))
        c.withdrow(amt)
        c.statement()
    elif option2=="E"or "e":
        sys.exit()
    else:
        print("Thanks For Using Application ")
print("Thanks For Using our Application")





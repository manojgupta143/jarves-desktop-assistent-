import sys
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def info(self):
        print("Id Of The Employee Is",self.eno)
        print("Name Of The Employee Is",self.ename)
        print("Salary  Of The Employee Is",self.esal)
    
class Attendence(Employee):
    def __init__(self,atendence):
        self.atendence=atendence
    def __div__(self):
        x=30
        dayPay=self.esal/x
        return dayPay
    def __mul__(self,other):
        pSal=self.dayPay*other.atendence
        return pSal
   

class OverTime(Attendence):
    def __init__(self, ot):
        self.ot=ot
    def __div__(self,other):
        super().__mul__(self)
        def __div__(self,other):
            hPay=self.dayPay/other.ot
            return hPay
        def __mul__(self,other):
            dOT=self.hPay*other.ot
            return dOT
e=Employee(100,"ashima",20000)
a=Attendence(25)
o=OverTime(25)
salary=(e*a)
ot=(a*o)
e.info()
print("Total Salary Of The Employee Is ",salary)
print("Over Time  Of The Employee Is ",ot)
print("The Grand Total Of The salary is ",salary+ot)
       


"""n=int(input("Enter No Of Employees :"))
for i in range(n):
    eno=input("Enter Employee No :")
    ename=input("Enter Name of Employee :")
    esal=int(input("Enter Employee Salary :"))"""

        
#fack employee data for data base testing
from random import *
alphabet="abcdefghijklmnopqrstuvwxyz"
digit="0123456789"
city=["Mumbai","Delhi",'Hydrabad',"Chennai","banglore"]
designation=["python developer","Softwere engineer","Project Manager","Django Developer"]
def fack_name():
  name=choice(alphabet).upper()
  n=randint(2,9)
  for i in range(n):
    name=name+choice(alphabet)
  return name
def fack_eno():
  eno="e-"
  for i in range(4):
    eno= eno+choice(digit)
  return eno
def fack_mno():
  mno="987"
  mno=choice(mno)
  for i in range(9):
    mno=mno+choice(digit)
  return mno
def fack_salary():
  salary=uniform(10000,50000)
  return salary
def fack_city():
  cyt=choice(city)
  return cyt
def fack_designaton():
  disg=choice(designation)
  return disg
def fack_em_data():
  print(f"The Name of Emloyee Is {fack_name()}")
  print(f"The Number of  Emloyee Is {fack_eno()}")
  print(f"The Mobile Number  of Emloyee Is {fack_mno()}")
  print("The Salary of Emloyee Is {:.2f}".format(fack_salary()))
  print(f"The City of Emloyee Is {fack_city()}")
  print(f"The Designation of Emloyee Is {fack_designaton()}")
     
option=int(input("Enter A Number How Many Fack Empoyee Data You Want To Generate :"))
for i in range(option):
  print("The Employee Data Is ")
  print()
  print(fack_em_data())
  print()
  





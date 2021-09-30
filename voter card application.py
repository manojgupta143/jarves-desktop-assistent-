dict = {}
print("Please Enter Your User Name And Password For Voter Card Apply :\n ")
user = input("Enter User Name :")
user.strip()
pwd = input("Enter Your password :")
pwd.strip()
dict[user] = pwd
print("Your User Name And password Saved Successfully \n ")
print("Please Varifie Your User Name And Password Again  ")
while True:
    users = input("Please Enter Your User Name :")
    pwds = input("Please Enter Your Password :\n")
    if users == user and pwds == pwd:
        print("Please Varifie Your Age ,You Are [ 18+]\n ")
        break
    else:
      print("Your User Name And Password Incurrect Please Enter Valid User Name And Password ")
      if user and pwds==5:
        print("You Tryed Enough Time Please Tyr Some Time later ") 
        break 
age = eval(input("Enter Your Age :\n"))
if age > 18:
   while True:
    print("You Are Eligibale For Vote \n ")
    print("Please Enter your All Detail \n")
    name = input("Enter Your Full Name :")
    mather = input("Enter Your Mather Name :")
    Father = input("Enter Your Father'S Name :")
    add = input("Enter Your Full Address :")
    ages = int(input("Enter Your Age :"))
    Village = input('Enter Village/ Town :')
    district = input("Enter Your District Name :")
    mark = input("Enter Your Body marks :")
    area = int(input("Enter Your Are PinCode"))
    state = input("Enter Your State Name :")
    feadbace = input("Press Yes To Save No for ReEnter , For Exit Press Any other Key")
    if feadbace.lower()=="yes":
      print("Your Data is Saved Succesfully ")
      print(f""" Your Data Is ....
      Your Name Is {name}
      Your Father's Name is {Father}
      Your Mather's Name Is {mather}
      Your Address Is {add}
      Your Age Is {age}
      Your Village Is {Village}
      Your District Is {district}
      Your mark Is {mark}
      Your Area  Is {area}
      Your State Is {state} """)
    elif "no"in feadbace :
      print("Please ReEnter Your Data ")
    else:
      break
else:
  print("Your Age is Not Eligibale For Vote Please Make Sure You Are 18 Years Old ")
   

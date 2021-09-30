n=int(input("Enter Number Of Student :"))
dict={}
i=1
for i in range(n):
    name=input("Enter Student Name ")
    marks=int(input('Enter Marks Of Student :'))
    dict[name]=marks
print("All Student Data stored Succesfull ")
while True:
    name=input("Enter The Name of Student For Getting his Marks :")
    if name in dict:
        print(f"The Name of The Student Is {name} And The Marks of Student {dict[name]}")
    else:
        print("Data Is Not Found ")
    option=input("Do You Want to Found Any Others Student data : [yes/ No] :")
    while option.lower()not in ["yes","no"]:
            option=input("Invalid option Please Choose a Valid Option [Yes Or No] :" )
    if option.lower() == "no":
           break
print("Thanks For Using our Service ")          
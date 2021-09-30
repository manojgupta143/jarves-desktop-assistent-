class Movie:
    def __init__(self,capacity):
        self.capacity=capacity
        self.costmers=[]
    def add_costmers(self,name):

        if not self.open_seat():
            return False
        self.costmers.append(name)
        return True
    def open_seat(self):
         return self.capacity-len(self.costmers)
n=int(input("Enter Capacity of Cinemaa :"))
f=Movie(n)
people=[]

while True:
    name=input("Enter Costmers Name :")
    people.append(name)
    print(f"Costmers{name} Added In Cinemaa Successfully")
    option=input("Do You Want to insert Mor costmers [Yes | No] :")
    if option.lower() =="no":
        break
for i in people:
    success=f.add_costmers(i)
if success:
    print(f"costmer {i} added to Cinemaa successfully")
else:
    print(f"not available seat for {i}")


    
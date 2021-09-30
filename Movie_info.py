class Movie:
    def __init__(self, title, hero, heroin, billian,):
        self.title = title
        self.hero = hero
        self.heroin = heroin
        self.billian = billian

    def info(self):
        print("The Name of Movie is ", self.title)
        print("The hero of Movie is ", self.hero)
        print("The Heroin of Movie is ", self.heroin)
        print("The Billian of Movie is ", self.billian)


listOfMovie = []
while True:
    name = input("Enter Movie name :")
    hero = input("Enter Hero  name :")
    heroin = input("Enter Heroin name :")
    billian = input("Enter billian name :")
    m = Movie(name,hero,heroin,billian)
    listOfMovie.append(m)
    option = input("Do You Want to Insert Of Another Movie Info :[Yes|No] :")  
    if option.lower() =="no":
        break
print("The Information of Movies ")
print("*"*50)
for list in listOfMovie:
    m.info()

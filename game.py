no=15
no_of_guess=1 
print("lets a play a game guess a number you have 8 chance to guess a number \n")
while(no_of_guess<=8):
    num=int(input("Enter a number:\n "))
    if num>15:
        print("You Entered a hight number please enter a low number: ")
    elif num<15:
        print("you entered a low number please enter a hight number\n")
    else:
        print("you win\n")
        print(8-no_of_guess,"you took to finish")
        break
    print(8-no_of_guess,"Number of guesses you have left")
    no_of_guess=no_of_guess+1
if(no_of_guess>8):
    print("game over: thanks for playing")
                
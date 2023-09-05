import random
print("Rock-Paper-Scissors Game:")
print("Winning Instructions rules for this game:-\n1.Rock vs Paper: Paper wins\n2.Rock vs Scissors: Rock wins\n3.Paper vs Scissors : Scissors wins")
print("\nGame starts:")
def user():
    print("1. Rock\n2. Paper\n3. Scissors\n")
    a=(input("Enter your choice(1,2,3): "))
    if a=="1":
     print("Rock")
    elif a=="2":
     print("Paper")
    elif a=="3":
     print("Scissors")
    else:
     print("Invalid Choice!\nEnter the valid choice:")
     user()
     return


    comp = ""
    comp+= random.choice("123")
    print("The computer's choice is: ", comp)
    if comp == "1":
        print("Rock")
    elif comp == "2":
        print("Paper")
    elif comp == "3":
        print("Scissors")
    print("--The Result is--")
    if a == comp:
     print("Tie")
    elif a == "1" and comp == "2":
     print("You Loose")
    elif a == "1" and comp == "3":
     print("Hurrah! You Win")
    elif a=="2" and comp=="1":
     print("Hurrah! You Win")
    elif a == "2" and comp == "3":
     print("You Loose")
    elif a=="3" and comp=="1":
     print("You Loose")
    elif a == "3" and comp == "2":
     print("Hurrah! You Win")

    def main():
        play_again=input("\nDo you want to play again?'(yes/no)':")
        if play_again=="yes":
            user()
            return
        elif play_again=="no":
            print("Exit the Game.\nThanks for playing..\nHave Fun.....")
        else:
            main()
            return
    main()
user()


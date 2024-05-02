import random
r="rock"
p="paper"
s="scissor"

def game(comp,user):
    
    if comp=='r':
        print("Comp chose",r)
        if user=='r':
            print("You chose",r)
            print("It's tie")
        elif user=='s':
            print("You chose",s)
            print("Computer Won")
        elif user=='p':
            print("You chose",p)
            print("You Won")
    elif comp=='s':
        print("Comp chose",s)
        if user=='r':
            print("You chose",r)
            print("You Won")
        elif user=='s':
            print("You chose",s)
            print("It's Tie")
        elif user=='p':
            print("You chose",p)
            print("Computer Won")
    elif comp=='p':
        print("Comp chose",p)
        if user=='r':
            print("You chose",r)
            print("Computer Won")
        elif user=='s':
            print("You chose",s)
            print("You Won")
        elif user=='p':
            print("You chose",p)
            print("It's tie")
    
while True:
    a=input("Type 'end' to exit the game or enter to play the game:\t")
    if a=='end':
        print("Thank you for playing")
        break
    else:
        user=input("Enter rock(r),paper(p),scessior(s):\t")
        print("You chose",r or p or s)

        random_no=random.randint(1,3)


        if random_no==1:
            comp="r"
        elif random_no==2:
            comp="p"
        elif random_no==3:
            comp="s"
        game(comp,user)
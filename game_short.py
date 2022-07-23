print("HELLO THERE")
print("IN THIS GAME YOU WILL HAVE TO GUESS THE WORD USING THE HINT GIVEN")
conformation = input("ARE YOU READY(Y/N):" )
if conformation == 'Y' :
    print("HERE IS YOUR HINT")
    print("I have branches but no fruit, trunk, or leaves. What am I?")
    print("REMEMBER YOU ONLY HAVE THREE CHANCES")
    print("ALL THE BEST")
elif conformation == 'N' :
    print("BYE-BYE")
    exit()
life_count = 3
answer = None
while answer == None :
    answer = input("ENTER YOUR ANSWER:")
    if answer == 'admin':
        for i in ["admin", "testing" , "won't" , "work"] :
            print(i)
            exit()
    while answer != 'bank' :
        life_count = life_count - 1
        print("NUMBER OF LIFE LEFT:" , life_count)
        if life_count <= 0 :
            print ("YOU HAVE LOST")
            break
        elif life_count > 0 :
            answer = input("ENTER YOUR ANSWER:")
            continue
if answer == 'bank' :
    print("YOU HAVE WON")

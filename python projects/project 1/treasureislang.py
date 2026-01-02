print("welcome to the treasure island game")
print("your mission is to find the treasure")
choice1 = input("you are at the corssroad where do you want to go type left or right : ")
if choice1 == "left":
    choice2 = input("you have come to a lake there is an isalnd in the middle of the lake type 'wait' to wait for a wait Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("you have arrive to the mansion: now there are three gate yellow,red,green. which colour do u choose: ").lower()
        if choice3 == "red":
            print("it is a room of fire you are dead bitch")
        
        elif choice3 == "yellow":
            print("aap bangaye crorepati:")
        
        elif choice3 == "green":
            print("nahi app maare gaye::")
        
        else:
            print("goli beta mjaak nahi:")
    else:
        print("maaro gayo dikro")

else:
    print("shh:")


        
     
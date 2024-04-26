import random
Colourlist = []
Winlist = []
P=0
Random_Colour_List = ["red","yellow","green","pink","black","white","blue","purple"]
Start = input("Do you wish to start?\n ---> press y ")
if Start == "y":
    print(Random_Colour_List)
    for i in range (4):
        print("Working")
        Colourlist.append(random.choice(Random_Colour_List))
        print("Guess 4 colours with spaces in between them")
        Guess = input (" --->")
        Splitguess = Guess.split()
        print(Splitguess)
if Splitguess == Colourlist: 
    print("You win \nthe list was",Colourlist,"good job!")
    for i in Splitguess
        
        
        
        
        
    

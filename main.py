#PHASE 1 - Goals For This are Lisstening for Player Input and Render the Changes on The Screen. Exit The Game When the Player Quits 
def menu():
    print("Start New Game - 1")
    print("Load Save File - 2")
    print("Game Settings  - 3")
    print("Quit Game      - 4")

print("The Uber's Sword")
menu() # Menu S
game_state = int(input("What Would You Like To Do - ")) #Type casting bercuase the input function always returns a string and therefore wouldnt be equal. 

while game_state != 4: #main game loop
    print("You Have Arrived at The Entrance of The Mages Castle") # This Should Only Appear Once
    userInput = input("What do you want to do? [W,A,S,D to move and Q to quit]: ")
    if userInput.lower() == "w":
        print("You have Moved Forward")

    elif userInput.lower() == "d":
        print("You have Moved to the Right")

    elif userInput.lower() == "s" :
        print("You have Moved Backward")

    elif userInput.lower() == "a":
        print("You have Moved to the Left")

    elif userInput.lower() == "q":
        print("You have Quit The Game")
        game_state = 4

#PHASE 2 - Creating an ASCII Map which represents the location of the chartacter, Let the player move around the world, Block Movement if collision with objects, Keep Updating player
#movement and map with every step taken 

#Map is made by making a map list which contains sub lists. The Number of Sub lists Depend on how many rows you want in you map. And the Amount of Tiles in the sublist are equal to 
#columns

"""print("#################")
print("#...............#")
print("#...............#")
print("#...............#")
print("#...............#")
print("#...............#")
print("#...............#") 
print("#################")"""

#I might not add a map as I dont think it is useful for me so I will not make a map right now and make it in the later stages if I want to have one in my game
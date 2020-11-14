import os
import random
hero_health=[100]
alive1=True
alive2=True
alive3=True
alive4=True
alive5=True
alive6=True
alive7=True
quest1=False
password=False
lantern=False
bone_club=False
Silver_key=False
Gold_key=False
Bronze_key=False
gameloop=True
dragon_alive=True
Items=[]

x = 1                 #y and x starting position. Remember 0,0 is top right corner. 
y = 3

dungeonMap = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
              ["0",".","7","0","0","£","£","£","£","£","£","0","£","£","£","£",".","0"],
              ["0",".",".","0","0","£","£","£","£","£","£","0","£","£","0",".",".","0"],
              ["0",".",".",".",".",".",".",".","0",".",".","!","£","£","0",".",".","0"],
              ["0",".",".","0","0",".",".",".","0",".",".","!",".",".","0",".",".","0"],
              ["0","0","0","0","0","0",".","0","0","0","0","0",".",".","0",".",".","0"],
              ["0","8",".",".","0",".",".",".","0",".",".","0",".",".","0",".","G","0"],
              ["0",".",".",".","0",".",".",".","0",".",".","0","0",".","0","0","0","0"],
              ["0",".",".",".","0",".",".",".","0",".",".","0","0",".","0",".",".","0"],
              ["0","0","0","!","!",".",".","9","0",".",".",".","1",".",".",".",".","0"],
              ["0","0","0","0","0",".",".","0","0",".",".","0","0",".","0",".",".","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0","0",".","0",".","S","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0",".",".","0","0","0","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0",".",".",".",".",".","0"],
              ["0",".","0","0",".",".","0","0","0",".","0","0",".",".",".","2",".","0"],  
              ["0",".",".","0",".",".","0","0",".",".",".","!",".",".","0","!","0","0"],
              ["0",".",".","0",".",".","0","0",".","B",".","!",".",".","0","!","!","0"],
              ["0",".",".","0",".",".","0","0",".",".",".","0",".",".","0","0","!","0"],
              ["0","5",".","0",".",".","3",".","4",".",".","0",".",".","6",".","E","0"],
              ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]]


playerMap  = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
              ["0",".",".","0","0",".",".",".",".",".",".","0",".",".",".",".",".","0"],
              ["0",".",".","0","0",".",".",".",".",".",".","0",".",".","0",".",".","0"],
              ["0","@",".",".",".",".",".",".","0",".",".","0",".",".","0",".",".","0"],
              ["0",".",".","0","0",".",".",".","0",".",".","0",".",".","0",".",".","0"],
              ["0","0","0","0","0","0",".","0","0","0","0","0",".",".","0",".",".","0"],
              ["0",".",".",".","0",".",".",".","0",".",".","0",".",".","0",".",".","0"],
              ["0",".",".",".","0",".",".",".","0",".",".","0","0",".","0","0","0","0"],
              ["0",".",".",".","0",".",".",".","0",".",".","0","0",".","0",".",".","0"],
              ["0","0","0","0","0",".",".",".","0",".",".",".",".",".",".",".",".","0"],
              ["0","0","0","0","0",".",".","0","0",".",".","0","0",".","0",".",".","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0","0",".","0",".",".","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0",".",".","0","0","0","0"],
              ["0",".",".",".",".",".",".","0",".",".",".","0",".",".",".",".",".","0"],
              ["0",".","0","0",".",".","0","0","0",".","0","0",".",".",".",".",".","0"],  
              ["0",".",".","0",".",".","0","0",".",".",".","0",".",".","0","0","0","0"],
              ["0",".",".","0",".",".","0","0",".",".",".","0",".",".","0","0","0","0"],
              ["0",".",".","0",".",".","0","0",".",".",".","0",".",".","0","0","0","0"],
              ["0",".",".","0",".",".",".",".",".",".",".","0",".",".",".",".","E","0"],
              ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]]

intro=["There is only the stench of death and decay here","You look for deadly traps but find none","You find nothing of interest here, maybe next time","You find nothing of interest here, and you hope that nothing finds an interest in you","You find nothing of interest here, you move ahead",
      "Stricken by grief, you wonder if you will ever leave this wicked dungeon","Wait..You hear something.. Or is it just the sound of your mind breaking..","These cold walls seems to drain even 'hope' itself","The darkness is overwhelming, how long can you last ?","You think you found something useful..You were mistaken",
      "You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on",
      "You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on",
      "You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on",
      "You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on","You find nothing of interest here, you continue on"]

def order(bag):
    for x in range(len(bag)): 
        print (x+1,bag[x]) 
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')   # For windows can just use os.system('cls')
    displayMap(playerMap) 

def alive_monster(enemy,damage,low,high,defense):
    global hero_health
    dead=False
    battle=True
    dam=str(damage)
    print("A",enemy,"see you!"," The",enemy,"attacks you on sight.")
    print("You take",dam, "damage")
    hh=hero_health[0]
    hh-=(damage)
    print (str(hh),"/100 health") 
    hero_health[0]=hh
    if hh<=0:
        dead=True

    if bone_club==True and dead==False:
        while battle==True:
            input("Press Enter to Attack")
            clear_screen()
            hit=random.randint(1,defense)
            if hit==1:
                break
            else:
                print("You strike the",enemy,"but it was not enough")
                print("The",enemy,"fights back !!")
                attack=random.randint(low,high)
                print("You take",str(attack),"damage")
                hh=hero_health[0]
                hh-=(attack)
                print (str(hh),"/100 health") 
                hero_health[0]=hh
                if hh<=0:
                    dead=True
                    break            

    if dead==True:
        print("Wounds upon wounds, you have fallen")
        input("           GAME OVER                ")
        input("Press enter to Exit game")
        exit()

    if bone_club==False:
        print("You need to escape and find a weapon to defeat the",enemy)    
    
def dead_monster(enemy):
    print("You see a",enemy,"dead on the floor ")

def displayMap(maps):    #Displaying the map
    for x in range(0,20):
        print(maps[x])

mapChoice = dungeonMap  #selecting a map

position = mapChoice[x][y]  #initialising the players position

print ("""
                              THE DUNGEON OF THE BLACK DRAGON
                              
Thrown into the dungeon of the black dragon for the entertainment of the elites.
You must fight through the horrors of the dungeon and find your escape.
May the light guide you !!!
""")
input("Press enter to begin your struggle")                                                                                         
clear_screen()
print("                                                                                      ")
print("         Instruction: Press 'Enter' after input to perform the action ")

while gameloop == True:
    
    previousX = x
    previousY = y
    playerMap[y][x] = "."
    print("                      ")
    print("Health:",hero_health[0])
    movement = input("W,S,D,A,ITEMS: ",).upper()
    
    if movement == "W":
        y = y-1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"

    if movement == "S":
        y = y+1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"
 
    if movement == "D":
        x = x+1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"

    if movement == "A":
        x = x-1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"
  
    if movement =="ITEMS":   
        playerMap[y][x] = "@"
        order(Items)
        input("press enter to continue")

    if position == "E":
         if  Silver_key ==True and Gold_key==True and Bronze_key==True:
             break
            
         else:    
             playerMap[y][x] = "E"
             x = previousX
             y = previousY
             playerMap[y][x] = "@"
             clear_screen()
             print("You reach the exit it seems to be locked ")
             print("You see 3 key holes on the door.")
             print(" Maybe this is a clue ")

    if position == "S":
        if Silver_key==False:
            clear_screen()
            input("You see a reflective glint in a pile of bones ")
            input("You find a Silver Key, it might be useful ")
            input("You pick up a Silver Key ")
            Silver_key=True
            Items.append("Silver Key")
        else:
            playerMap[y][x] = "@"
            clear_screen()
            print("There is nothing of importance in this area")

    if position=="G":
        if Gold_key==False and bone_club==True:
             playerMap[y][x] = "R"
             x = previousX
             y = previousY
             playerMap[y][x] = "@"
             clear_screen()
             print("You see a Rag man")
             print("He asks you if you want to make a trade")
             print ("He presents a Gold Key and wants your bone club")
             decision1=input("Make the trade ? Yes or No")
             decision=decision1.lower()

             if decision=="y" or decision=="yes":
                 print("Ok lets trade")
                 Items.append("Gold Key")
                 Gold_key=True
                 Items.remove("Bone Club")
                 bone_club=False
                 print("The trade is complete, enjoy your Key..")
           
             else:
                print("come back if you change your mind")               
        else:
            playerMap[y][x] = "R"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen()
            print("You see a Rag man, he said he is a trader")
            print("He is looking for weapons to buy ")
            
    if position == "B":
        currentX=x
        currentY=y
        if alive7==True:
               playerMap[y][x] = "K"
               x = previousX
               y = previousY
               playerMap[y][x] = "@"
               clear_screen()
               alive_monster("Fallen Knight",random.randint(10,15),1,5,3)
        
               if bone_club==True:
                   input("The Fallen Knight has fallen..Again ")
                   input("You find a Bronze Key on the dead Knight")
                   input("You pick up a Bronze Key")
                   playerMap[currentY][currentX]="X"
                   Bronze_key=True
                   Items.append("Bronze Key")
                   alive7=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Fallen Knight")
          
    if position == "0": 
        playerMap[y][x] = "0"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen()
        print("You are at a wall and you cannot pass.")

    if position == "£":
        if lantern==False:
            playerMap[y][x] = "."
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen()
            print("The darkness here is much too great. You step back to find another way")
        else:
            playerMap[y][x] = "@"
            clear_screen()
            print(" The lantern's warm glow pacifies even the darkest shadows. You move ahead")  

    if position == "!":
        if password==False:
            playerMap[y][x] = "0"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen()
            print("You are at a wall and you cannot pass")

        else:
            playerMap[y][x] = "@"
            clear_screen()
            print(" You found a secret passageway, you journey ahead") 
     
    if position == ".":
        playerMap[y][x] = "@"
        clear_screen()
        intro1=random.choice(intro)
        print (intro1)
        print("which direction will you go ?")  
        
    if position == "1":
        currentX=x
        currentY=y
        if alive1==True:
               playerMap[y][x] = "G"
               x = previousX
               y = previousY
               playerMap[y][x] = "@"
               clear_screen()
               alive_monster("Hungry Ghoul",random.randint(15,25),10,15,5)
               
               if bone_club==True:
                   print("You smash the Ghoul in the ribs with such force")
                   print("splitting the Ghoul in half, he is hungry no more ")
                   playerMap[currentY][currentX]="X"
                   alive1=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Ghoul")

    if position == "2":
        currentX=x
        currentY=y
        if alive2==True:
            playerMap[y][x] = "I"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen()
            alive_monster("Deranged Bog Imp",random.randint(5,15),2,8,3)
           
            if bone_club==True:
                print("You viciously strike the Bog Imp again and again")
                print("until it is just a pulp of flesh")
                playerMap[currentY][currentX]="X"
                alive2=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Bog Imp")

    if position == "3":
        currentX=x
        currentY=y
        if alive3==True:
            playerMap[y][x] = "I"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen()
            alive_monster("Psychotic Bog Imp",random.randint(5,15),2,8,3)

            if bone_club==True:
                print("You smash your club into the Imp's legs")
                print("tearing both limbs clean off and then deliver the kiling blow" )
                playerMap[currentY][currentX]="X"
                alive3=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Bog Imp")

    if position == "4":
        currentX=x
        currentY=y
        if alive4==True:
               playerMap[y][x] = "G"
               x = previousX
               y = previousY
               playerMap[y][x] = "@"
               clear_screen()
               alive_monster("Mutant Ghoul",random.randint(15,25),10,15,5)
               
               if bone_club==True:
                   print("You smash the Ghoul in the face with your bone club")
                   print("killing it with a mighty blow")
                   playerMap[currentY][currentX]="X"
                   alive4=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Mutant Ghoul")

    if position == "5":
        currentX=x
        currentY=y
        if alive5==True:
               playerMap[y][x] = "A"
               x = previousX
               y = previousY
               playerMap[y][x] = "@"
               clear_screen()
               alive_monster("Putrid Abomination",random.randint(5,20),3,8,4)
            
               if bone_club==True:
                   print("You strike the Abomination's head with your club")
                   print("splattering his brains on the walls")
                   playerMap[currentY][currentX]="X"
                   alive5=False
                   quest1=True
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Unholy Abomination")

    if position == "6":
        currentX=x
        currentY=y
        if alive6==True:
               playerMap[y][x] = "D"
               x = previousX
               y = previousY
               playerMap[y][x] = "@"
               clear_screen()
               alive_monster("Black Dragon",random.randint(20,35),15,20,10)
               
               if bone_club==True:
                   print("You crack the Dragon's Skull, with a devastating blow")
                   print("The Dragon falls to the ground dead")
                   print("You notice piles of gold and treasure scatter across the floor ")
                   print("You must come back to gather some, once you find the exit")
                   dragon_alive=False 
                   playerMap[currentY][currentX]="X"                   
                   alive6=False
        else:
            playerMap[y][x] = "@"
            clear_screen()
            dead_monster("Black Dragon")
              
    if position == "7":
            if bone_club==False:
                clear_screen()
                input("You search amongst the piles of dead bodies ")
                input("You find a large bone that could be used as a club")
                input("You pick up a bone club ")
                bone_club = True
                Items.append("Bone Club")
            else:
                playerMap[y][x] = "@"
                clear_screen()
                print("There is nothing of importance in this area")

    if position == "8":
            if lantern==False:
                clear_screen()
                input("In the distance you see a dim light")
                input("As you walk closer you see a lantern next to a decomposing corpse")
                input("You pick the lantern up. The lantern's soft glow is 'comforting'")
                lantern = True
                Items.append("Lantern")
            else:
                playerMap[y][x] = "@"
                clear_screen()
                print("There is nothing of importance in this area")

    if position == "9":
        if quest1==False:
           playerMap[y][x] = "W"
           x = previousX
           y = previousY
           playerMap[y][x] = "@"
           clear_screen()           
           print("You see a Mad Wizard in front of you")
           print("He screams 'Kill the Putrid Abomination !!' ")
           print("'He has stolen my eyes, ghost and toes !!'")
           print("'and I will help you escape this tea house of doom'")
           print("'The princess is south west from here, brave donkey'")
        else:
           playerMap[y][x] = "W"
           x = previousX
           y = previousY
           playerMap[y][x] = "@"
           clear_screen()
           print("You see a Mad Wizard in front of you") 
           print("He thanks you for slaying the Putrid Abomination")
           print("and tell you how to look out for secret passages ")
           print("He points WEST to show you one of them")
           print("[You now have access to all secret passages]")
           password=True

if dragon_alive==False:
    print("                                                         ")
    print("You have slayed the Black Dragon and escaped the dungeon ")
    print("You have upset the elites but they grudgingly offer your reward. Your freedom'")
    print("With a bagful of the dragon's treasure, you walk away filthy rich. Thank you for playing ")
    input("Press enter to exit")
else:
    print("                                                         ")        
    print("You unlock the door and is granted your reward. 'Freedom'")
    print("You have escaped the Dungeon of the Black Dragon. Thank you for playing ")
    input("Press enter to exit")
                                                        ###https://github.com/Ninedeadeyes/Dungeon-of-the-Black-Dragon

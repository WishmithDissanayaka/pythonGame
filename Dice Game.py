#Import the necessary modules
try:
    from tabulate import tabulate
except:
    print("Tabulate isn't installed on your device.\nINSTRUCTIONS\n1:Open command prompt\n2:Type pip install tabulate\n3:Re-run the program after installing")
import datetime
import time
import random

#Variables
username=0
playerstart=0
compstart=0
playerposition=0
compposition=0
playermoves = 0
compmoves = 0
playerblackhole = 0
compblackhole = 0

#Date and Time
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
date = "{}_{}_{}_{}_{}".format(day,month,year,hour,minute)

#Table specification
table_arrangement = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                     ["","","","","","","0","","","","","","","0","","","","","",""],
                     ["","","","","","","0","","","","","","","0","","","","","",""]]

#Functions
def player():
    player=random.randint(1,6)
    if player != 6:
        print("Human dice roll is",player,"and cannot start the game")
    else :
        print("Human dice roll is 6 and the player has entered the board")
        return player

def computer():
    computer=random.randint(1,6)
    if computer != 6:
        print("Computer dice roll is",computer,"and cannot start the game")
    else:
        print("Computer dice roll is 6 and the computer has entered the board")
        return computer

#Start of the program
username=input("Please enter your name : ")
print("\nWelcome to '20x2'",username)
print("'20x2' is a board game where you play against the computer and try to reach the 20th slot to win."
      "\n\nRULES\n1. To enter the board, you must continually roll until you land a 6."
      "\n2. After landing a 6, you may enter the game board."
      "\n3. The number of moves is equal to half of the dice's value (odd nums have the '.5' neglected)."
      "\n4. Block 7 and block 14 are black holes."
      "\nIF YOU LAND ON A BLACK HOLE YOU WILL BE SENT BACK TO BLOCK 1."
      "\n\nPlay and win against the computer.\nGOOD LUCK!!")

while True:
    Start=input("\nEnter 'r' to roll the dice: ")
    if(Start!='r'):
        print("Please enter 'r'")
        continue
    if(Start=="r"):
        if(playerstart==False):
            if (player()==6):
                playerstart=True
                playerposition=1
                playermoves = playermoves + 1
        else:
            previouspos = playerposition
            roll = random.randint(1,6)
            currentpos = roll//2
            playerposition = previouspos + currentpos
            if(playerposition>20):
                playerposition=20
            print("Human dice roll is",roll,"and current location is",playerposition)
            playermoves = playermoves + 1

        if(compstart==False):
            if(computer()==6):
                compstart=True
                compposition=1
                compmoves = compmoves + 1
                while True:
                    compposition=1
                    break
        else:
            while True:
                comppreviouspos = compposition
                roll = random.randint(1,6)
                comppos = roll//2
                compposition = comppreviouspos + comppos
                if(compposition>20):
                    compposition=20
                print("Computer dice roll is",roll,"and current location is",compposition)
                compmoves = compmoves + 1
                break

        #If the player is not on the board and the computer is on the board
        if(playerstart==False and compstart==True):
            if(compposition==7 or compposition==14):
                print("The Computer has hit a blackhole and has been sent back to location 1")
                compposition=1
                compblackhole= compblackhole + 1

            compposition=min(compposition, 20)
            
            row_2 = 0
            column_1 = 0

            row_3 = 3
            column_2 = compposition

            new_value1 = "X"
            new_value2 = " "
            none =" "

            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        new_value2, new_value1

            table = tabulate(table_arrangement, headers="firstrow",tablefmt="fancy_grid")
            print(table)
            
            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        none, none

        #If the player is on the board and the computer is not on the board
        if(playerstart==True and compstart==False):
            if(playerposition==7 or playerposition==14):
                print("The Player has hit a blackhole and has been sent back to location 1")
                playerposition=1
                playerblackhole= playerblackhole + 1

            playerposition= min(playerposition, 20)
            
            row_2 = 2
            column_1 = playerposition

            row_3 = 0
            column_2 = 0

            new_value1 = " "
            new_value2 = "X"
            none=" "

            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        new_value2, new_value1

            table = tabulate(table_arrangement,headers="firstrow",tablefmt="fancy_grid")
            print(table)
            
            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        none, none

        #If the player is on the board and the computer is on the board
        if(playerstart==True and compstart==True):
            if(compposition==7 or compposition==14):
                compposition=1
                print("The computer has hit a blackhole and has been sent back to location 1")
                compblackhole= compblackhole + 1

            if(playerposition==7 or playerposition==14):
                playerposition=1
                print("The player has hit a blackhole and has been sent back to location 1")
                playerblackhole= playerblackhole + 1

            if playerposition>=20:
                playerposition=min(playerposition, 20)
                
            if compposition>=20:
                compposition=min(compposition, 20)

            row_2 = 2
            column_1 = playerposition


            row_3 = 3
            column_2 = compposition

            new_value1 = "X"
            new_value2 = "X"
            none=" "

            
            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        new_value2, new_value1

            table = tabulate(table_arrangement, headers="firstrow",tablefmt="fancy_grid")
            print(table)

            table_arrangement[row_2-1][column_1-1], table_arrangement[row_3-1][column_2-1] = \
                        none, none

        if(playerposition>=20):
            print("You win")
            break

        if(compposition>=20):
            print("The computer wins")
            break

#Text file inputs
with open(date + '.txt','w') as fo:
    computer_moves_txt = repr(compmoves)
    computer_blackhole_hits= repr(compblackhole)
    fo.write("Computer")
    fo.write("\nTotal Moves:" + computer_moves_txt)
    fo.write("\nBlackhole Hits:"+ computer_blackhole_hits)

    if(compposition>=20):
        fo.write("\nWon the game")
    else:
        fo.write("\nLost the game")

    player_moves_txt = repr(playermoves)
    player_blackhole_hit_times = repr(playerblackhole)
    fo.write("\n\n"+username)
    fo.write("\nTotal Moves:" + player_moves_txt)
    fo.write("\nBlackhole hits:" + player_blackhole_hit_times)

    if(playerposition>=20):
        fo.write("\nWon The game")
    else:
        fo.write("\nLost The Game")

time.sleep(6)
quit()

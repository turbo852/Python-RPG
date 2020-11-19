#RPG

import string, random, pickle, os.path
from os import path

#TODO:
#Make enemy groups
#Make battle system flow
#Make equipment system
#Make story system
#make take command work with items two words in length

inventory = []

def resetCurrentRoom(currentRoom):
    currentRoom = 1
    return currentRoom

def showInstructions():
    print("========================")
    print("Welcome to Python RPG!")
    print("========================")

def showStatus():
    print("\n")
    showMap()
    print("\n========================")
    print("You are in " + rooms[currentRoom]["name"])
    print("------------------------")
    #story
    if "init" in rooms[currentRoom] and rooms[currentRoom]["initSwitch"] == "on":
        print(rooms[currentRoom]["init"])
        rooms[currentRoom]["initSwitch"] = "off"
        print("------------------------")
    #directions
    if "east" in rooms[currentRoom]:
        print("There is a door to the east.")
    if "west" in rooms[currentRoom]:
        print("There is a door to the west.")
    if "north" in rooms[currentRoom]:
        print("There is a door to the north.")
    if "south" in rooms[currentRoom]:
        print("There is a door to the south.")
    if "up" in rooms[currentRoom]:
        print("There is a staircase leading up to the next floor.")
    if "down" in rooms[currentRoom]:
        print("There is a staircase leading down to the next floor.")
    print("------------------------")
    for item in player:
        print(player[item]["name"] + " HP: " + str(player[item]["currhp"]) + "/" + str(player[item]["maxhp"]))
    print("Gold: " + str(player[1]["gold"]))
    print("------------------------")
    print("Inventory: ")
    for item in inventory:
        print(item)
    if "item" in rooms[currentRoom]:
        print("------------------------")
        print("You see a " + rooms[currentRoom]["item"])
    if "dropped" in rooms[currentRoom]:
        print("------------------------")
        print("You see a " + rooms[currentRoom]["dropped"] + " that was dropped.")
        #length = len(rooms[currentRoom]["dropped"]) - 1
        #if length > 0:
        #    for item in rooms[currentRoom]["dropped"]:
        #        print("You see a " + str(rooms[currentRoom]["dropped"][length][item]) + " that was dropped!")
        #else:
        #    length = len(rooms[currentRoom]["dropped"])
        #    print("You see a " + str(rooms[currentRoom]["dropped"][0]) + " that was dropped!")          
    print("------------------------")
    if "monster" in rooms[currentRoom]:
        print("There is a " + rooms[currentRoom]["monster"] + " in this room.")
        print("------------------------")
        #Set up chance that battle starts immediately with ambush attack, else enter battle via command
        totalAgility = 0
        for item in player:
            totalAgility += player[item]["agility"]
        averageAgility = totalAgility / len(player)
        if monsters[rooms[currentRoom]["monster"]]["agility"] > averageAgility:
            ambush = random.randint(1,99)
            if ambush > 30:
                print("Ambush attack!")
                battleStart(currentRoom, rooms[currentRoom]["monster"])
    #sign
    if "sign" in rooms[currentRoom]:
        print("There is a sign in this room.")
        print("------------------------")
    print("------------------------")
    print("------------------------")
    print("Commands: ")
    print("'go [direction]'")
    print("'take [item]'")
    print("'use [item] [direction/object]'")
    print("'fight [monstername]'")
    print("'drop [item]'")
    print("'equip [item] [player]'")
    print("'read [sign]'")
    print("------------------------")    

def enemyAttack(currentRoom, monster, playerNo):
    #choose which player to attack
    target = random.randint(1,(len(player)))
    #check if target is already dead
    while player[target]["currhp"] <= 0:
        print("Pick new target")
        target = random.randint(1,(len(player)))
    #check for dodge
    dodge = ((monsters[rooms[currentRoom]["monster"]]["agility"] / player[target]["agility"]) / 100) * random.randint(0,100)
    print(dodge)
    if dodge < 0.32:
        print(rooms[currentRoom]["monster"] + " missed!")
        battleOn = True
        return battleOn
    else:
        damage = (monsters[rooms[currentRoom]["monster"]]["strength"] - player[target]["defense"]) * random.randint(0,1)
        #check if target is defending
        if target == playerNo:
            damage = round(damage / 2)
            print(player[playerNo]["name"] + " defended successfully!")
        elif damage <= 0:
            damage = 1
        #take damage
        player[target]["currhp"] -= damage
        print(rooms[currentRoom]["monster"] + " attacks " + player[target]["name"] + " for " + str(damage) + " damage!")
        print(player[target]["name"] + " HP: " + str(player[target]["currhp"]))
        #check if player died
        if player[target]["currhp"] <= 0:
            print(player[target]["name"] + " has died...")
            #check if party has died
            battleOn = partyDead(currentRoom, rooms[currentRoom]["monster"])
            return battleOn
        else:
            battleOn = True
            return battleOn

def playerAttack(currentRoom, monster, playerNo):
    damage = player[playerNo]["strength"] - monsters[rooms[currentRoom]["monster"]]["defense"] + random.randint(0,1)
    if damage <= 0:
        damage = 1
    #check for dodge
    dodge = ((player[playerNo]["agility"] / monsters[rooms[currentRoom]["monster"]]["agility"]) / 100) * random.randint(0,100)
    print(dodge)
    if dodge < 0.32:
        print(player[playerNo]["name"] + " missed!")
        print("------------------------")
        battleOn = True
        return battleOn
    else:
        #check for critical hit
        crit = player[playerNo]["luck"] / 5
        crit = int(crit)
        if 99 - crit < random.randint(0,100):
            damage *= 2
            print("Critical hit!")
        monsters[rooms[currentRoom]["monster"]]["currhp"] -= damage
        print(player[playerNo]["name"] + " hit " + rooms[currentRoom]["monster"] + " for " + str(damage) + " damage!")
        print("------------------------")
        #check if monster is dead
        if monsters[rooms[currentRoom]["monster"]]["currhp"] <= 0:
            battleOn = monsterDefeated(currentRoom, rooms[currentRoom]["monster"])
            #restore monster
            monsters[rooms[currentRoom]["monster"]]["currhp"] = monsters[rooms[currentRoom]["monster"]]["maxhp"]
            return battleOn
        else:
            battleOn = True
            return battleOn

def partyDead(currentRoom, monster):
    numDead = 0
    for item in player:
        print("player: " + str(item))
        if player[item]["currhp"] <= 0:
            numDead += 1
            print("numDead: " + str(numDead))
            print("length of player: " + str(len(player)))
            #check if entire party is dead
            #if entire party is dead return False
            if numDead == len(player):
                print("Battle over!")
                print("The party has failed...")
                #restore players
                for num in player:
                    player[num]["currhp"] = 1
                #take half of the party's gold
                player[1]["gold"] = round(player[1]["gold"] / 2)
                battleOn = False
                print("currentRoom: " + str(currentRoom))
                print("battleOn party dead: " + str(battleOn))
                return battleOn
        #if party member is alive return True
        if item == len(player):
            print("item: " + str(item))
            battleOn = True
            print("battleOn party not dead: " + str(battleOn))            
            return battleOn

def monsterDefeated(currentRoom, monster):        
    if monsters[rooms[currentRoom]["monster"]]["currhp"] <= 0:
        print(monsters[rooms[currentRoom]["monster"]]["name"] + " has been defeated!")
        print("Battle over!")
        gain = monsters[rooms[currentRoom]["monster"]]["exp"]
        for item in player:
            player[item]["exp"] += gain
            player[item]["next"] -= gain
            print(player[item]["name"] + " " + str(gain) + " exp gained!")
            leveled = checkLevel(item)
        if leveled is False:
            for item in player:
                print(player[item]["name"] + " exp to next level: " + str(player[item]["next"]))
        gain = monsters[rooms[currentRoom]["monster"]]["gold"]
        player[1]["gold"] += gain
        print(str(gain) + " gold found!")
        #chance for monster to drop item
        gain = random.randint(1,100)
        if gain > 1:
            #add item to end of inventory
            inventory[-1:] += [monsters[rooms[currentRoom]["monster"]]["item"]]
            print(monsters[rooms[currentRoom]["monster"]]["name"] + " dropped " + monsters[rooms[currentRoom]["monster"]]["item"])
        print("------------------------")
        battleOn = False
        return battleOn

def rollGain(item):
    gain1 = random.randint(0,10) * player[item]["luck"] / 10
    print(gain1)
    gain1 = round(gain1)
    return gain1

def checkLevel(item):
    if player[item]["next"] <= 0:
        leveled = True
        #check level cap
        if player[item]["level"] == 13:
            player[item]["next"] = 999999
        else:
            player[item]["level"] += 1
            print(player[item]["name"] + " is now level " + str(player[1]["level"]) + "!")
            player[item]["next"] = nextLevel[player[item]["level"]]
            print("Exp to next level: " + str(player[item]["next"]))
            #Raise stats
            gain = random.randint(0, 100) / 10 + 1
            print(gain)
            gain = round(gain)
            print("HP +" + str(gain) + "!")
            player[item]["maxhp"] += gain
            player[item]["currhp"] = player[item]["maxhp"]
            gain = rollGain(item)
            if gain > 0:
                print("Strength +" + str(gain) + "!")
                player[item]["strength"] += gain
            gain = rollGain(item)
            if gain > 0:
                print("Defense +" + str(gain) + "!")
                player[item]["defense"] += gain
            gain = rollGain(item)
            if gain > 0:
                print("Agility +" + str(gain) + "!")
                player[item]["agility"] += gain
            gain = rollGain(item) - 1
            if gain > 0:
                print("Luck +" + str(gain) + "!")
                player[item]["luck"] += gain
            return leveled
    else:
        leveled = False
        return leveled

def displayEnemyHP():
    currentHP = monsters[rooms[currentRoom]["monster"]]["currhp"]
    maxHP = monsters[rooms[currentRoom]["monster"]]["maxhp"]
    temp = round(currentHP/maxHP*10)
    diff = 10 - temp
    print(monsters[rooms[currentRoom]["monster"]]["name"])
    print("HP: [", end="")
    while temp > 0:
        print("=", end="")
        temp -= 1
    while diff > 0:
        print(" ", end="")
        diff -= 1
    print("]")

def battleStatus():
    for item in player:
        print("Name: " + player[item]["name"])
        print("Level: " + str(player[item]["level"]))
        print("HP: " + str(player[item]["currhp"]) + "/" + str(player[item]["maxhp"]))
        print("Strength: " + str(player[item]["strength"]))
        print("Defense: " + str(player[item]["defense"]))
        print("Agility: " + str(player[item]["agility"]))
        print("Luck: " + str(player[item]["luck"]))
        print("------------------------")


        
def battleStart(currentRoom, monster):
    print("------------------------") 
    print("Battle started!")
    print("------------------------")
    battleOn = True
    while battleOn == True:
        battleStatus()

        for item in player:
           #exit battle if battle is over
            if battleOn is False:
                print("battleOn = " + str(battleOn))
                break
            #check if player is dead
            if player[item]["currhp"] <= 0:
                print("pick next player")
                item += 1
                if item <= len(player):
                    continue
                else:
                    break
            displayEnemyHP()
            print("------------------------")
            print(player[item]["name"] + " is up!")
            
            print("------------------------")
            print("Commands: ")
            print("'attack [monster]'")
            print("'defend'")
            print("'use [item] [playerName]'")
            print("'run'")
            print("------------------------") 

          
            #select moves for each player
        
               
            move = input(">").split()
            print("\n")
            print("\n")
            print("\n")
            #catch if nothing is entered.
            if len(move) == 0:
                print("Please enter a valid command.")
            #========= attack =========
            elif move[0] == "attack":
            #catch if only attack is entered.
                if len(move) == 1:
                    print("Please specify what to attack.")
                #catch if monster not in room
                elif move[1] not in rooms[currentRoom]["monster"]:
                    print("That monster is not in the room.")
                    print("------------------------")
                    print(rooms[currentRoom]["monster"] + " gets in a surprise attack while you were bumbling around!")
                    battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
                    print("battleOn no mon = " + str(battleOn))
                    print("------------------------")
                #attack monster
                elif move[1] in rooms[currentRoom]["monster"]:
                    #decide who attacks first
                    if monsters[rooms[currentRoom]["monster"]]["agility"] > player[item]["agility"]:
                        battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
                        print("battleOn = " + str(battleOn))
                        if battleOn is True:
                            battleOn = playerAttack(currentRoom, rooms[currentRoom]["monster"], item)
                            print("battleOn = " + str(battleOn))
                    else:
                        battleOn = playerAttack(currentRoom, rooms[currentRoom]["monster"], item)
                        if battleOn is True:
                            battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
                            print("battleOn = " + str(battleOn))
            #========= defend =========
            elif move[0] == "defend":
                print(player[item]["name"] + " defends.")
                battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], item)
                print("battleOn = " + str(battleOn))
            #========= use =========
            elif move[0] == "use":
                #catch if only use is entered.
                if len(move) == 1:
                    print("Please specify what to use.")
                #catch if item not in inventory.
                elif move[1] not in inventory:
                    print("You do not have a " + move[1])
                #catch if direction not specified.
                elif len(move) == 2:
                    print("Please specify who to use the " + move[1] + " on.")
                #use item
                #use potion
                elif move[1] == "potion":
                    #catch if no target is given
                    if len(move) < 2:
                        print("Please specify who will drink the potion.")
                    #check if target is a valid party member
                    if searchDict(player, move[2]):
                        print("That is not a party member!\n")
                    else:
                        if str(player[item]["name"]) != move[2]:
                            print(player[item]["name"] + " gives the " + move[1] + " to " + move[2])
                        healPlayer(move[2])
                        inventory.remove("potion")
            #========= run =========
            elif move[0] == "run":
                print(player[item]["name"] + " is a whuss.")
                print("...but let's see if " + player[item]["name"] + " can escape anyway.")
                escape = int((player[item]["agility"] / monsters[rooms[currentRoom]["monster"]]["agility"]) * random.random() * 100)
                print("Escape: " + str(escape))
                #if player is faster
                if player[item]["agility"] >= monsters[rooms[currentRoom]["monster"]]["agility"]:
                    #give player a good chance to escape
                    if escape > 25:
                        #player escapes
                        print("The party escaped!")
                        battleOn = False
                    else:
                        #player fails to get away
                        print(player[item]["name"] + " was too slow!")
                        battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
                #if enemy is faster
                else:
                    #make it hard for the player to escape
                    if escape > 50:
                        #player escapes
                        print("The party escaped!")
                        battleOn = False
                    else:
                        #player fails to get away
                        print(player[item]["name"] + " was too slow!")
                        battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
            #catch if invalid command entered
            else:
                print("------------------------")
                print("Please enter a valid command.")
                print("------------------------")
                print(rooms[currentRoom]["monster"] + " gets in a surprise attack while you were bumbling around!")
                battleOn = enemyAttack(currentRoom, rooms[currentRoom]["monster"], 0)
                print("battleOn no move = " + str(battleOn))
                print("------------------------")
            
def saveGame():
    fi = open("rpgsave.pkl", "bw")
    playerSave = player
    playerInventory = inventory
    pickle.dump(playerSave,fi)
    pickle.dump(playerInventory,fi)
    fi.close()          
    print("Game saved successfully!")

def saveInventory():
    fi = open("rpginv.pkl", "bw")
    playerInventory = inventory
    pickle.dump(playerInventory,fi)
    fi.close()          

def loadGame(player):
    print("Player data: ")
    print(str(player))
    fi = open("rpgsave.pkl", "rb")
    tempPlayer = pickle.load(fi)
    print("Game loaded successfully!")
    return tempPlayer

def loadInventory(inv):
    print("Player inventory: ")
    print(str(inventory))
    fi = open("rpginv.pkl", "rb")
    tempInv = pickle.load(fi)
    return tempInv

def saveRooms(filename,roomSet):
    print(filename)
    print(roomSet)
    #create filename string
    newRooms = str(filename) + ".pkl"
    #newCurrentRoom = str(filename) + "currentroom.pkl"
    newCurrentRoom = "currentroom.pkl"
    print(newCurrentRoom)
    fi = open(newRooms, "bw")
    pickle.dump(roomSet,fi)
    fi.close()
    fi = open(newCurrentRoom, "bw")
    pickle.dump(currentRoom,fi)
    fi.close()

def loadRooms(filename):
    #create filename string
    newRooms = str(filename) + ".pkl"
    print("Rooms: ")
    #print(newRooms)
    try:
        fi = open(newRooms, "rb")
    #except FileNotFoundError:
     #   print("That's not a valid roomset name!")
      #  raise
    except IOError:
        print('Cannot load', newRooms)
    else:
        print(newRooms, 'loaded successfully!')
        tempRooms = pickle.load(fi)
        print("New rooms loaded successfully!")
        return  tempRooms
    

def loadCurrentRoom(newCurrentRoom):
    fi = open(newCurrentRoom, "rb")
    tempCurrentRoom = pickle.load(fi)
    return tempCurrentRoom

def showMap():
    print("Map:",end="")
    #get row
    row = int(currentRoom / 5)
    #get column
    column = currentRoom % 5
    #print Coordinates
    #catch when in column 5
    if column == 0:
        row -= 1
        print(" " + str(row + 1) + ", 5")
    else:
        print(" " + str(row + 1) + ", " + str(column))
    #setup temporary count
    count = row
    #print rows before current location
    while count > 0:
        print("[-----]")
        count -= 1
    #print location
    if column == 0:
        print("[----*]")
    elif column == 4:
        print("[---*-]")
    elif column == 3:
        print("[--*--]")
    elif column == 2:
        print("[-*---]")
    elif column == 1:
        print("[*----]")
    #print rows after current location
    count = 4 - row
    while count > 0:
        print("[-----]")
        count -= 1

def searchDict(values, search):
    for item in values:
        for j in values[item]:
            if search in j:
                return item
    return None

def healPlayer(char):
    for item in player:
        if char == player[item]["name"]:
            print(str(player[item]["name"]) + " drank the potion.\n")
            player[item]["currhp"] = player[item]["maxhp"]
            print(player[item]["name"]+ " has been healed!\n")
            print(player[item]["name"] + ": " + str(player[item]["currhp"]) + "/" + str(player[item]["maxhp"]))
      

nextLevel = [0, 10, 20, 35, 50, 85, 115, 175, 275, 400, 500, 650, 800, 1000]

droppable = ["cookie", "potion", "sword", "goo", "imp hat", "goblin cap", "coin", "broken wing"]

weapon = ["sword", "knife", "dagger", "staff", "rapier", "cutlass", "scimitar", "hammer", "mace"]

helm = ["cap", "leather cap", "bronze helmet", "iron helmet", "steel helmet", "wooden helmet"]

armor = ["leather tunic", "chain mail", "shirt", "iron mail", "steel mail", "bronze mail", "iron armor", "bronze armor", "steel armor"]

acc = ["brass ring", "copper ring", "iron ring", "bandana", "silver ring", "gold ring", "ruby ring", "emerald ring", "sapphire ring", "diamond ring"]

rooms = { 1 : { "name" : "the Hall" ,
                "east" : 2 ,
                "south" : 6} ,
          
          2 : { "name" : "the Bedroom" ,
                "west" : 1 ,
                "south" : 7 ,
                "item" : "sword" ,
                "east" : 3 } ,
          
          6 : { "name" : "the Kitchen" ,
                "north" : 1 ,
                "monster" : "imp" ,
                "item" : "cookie" } ,
          
          7 : { "name" : "the Bathroom" ,
                "north" : 2 ,
                "monster" : "slime" ,
                "item" : "key" } ,
          
          3 : { "name" : "the Dining Room" ,
                "west" : 2 ,
                "east" : "lock" ,
                "item" : "key" } ,

          4 : { "name" : "the Bedroom 2" ,
                "west" : 3 ,
                "east" : 5 ,
                "item" : "key" },
          
          5 : { "name" : "the Closet" ,
                "west" : 4 ,
                "south" : 10 ,
                "item" : "potion" },
          
          10 : { "name" : "the Secret Room" ,
                "north" : 5 ,
                "monster" : "bat" ,
                "item" : "coin" } }

monsters = { "slime" : { "name" : "slime" ,
                       "maxhp" : 3 ,
                       "currhp" : 3 ,
                       "strength" : 2 ,
                       "defense" : 1 ,
                       "agility" : 3 ,
                       "exp" : 5 ,
                       "gold" : 1 ,
                       "item" : "goo" } ,
             
             "blob" : { "name" : "blob" ,
                       "maxhp" : 3 ,
                       "currhp" : 3 ,
                       "strength" : 2 ,
                       "defense" : 1 ,
                       "agility" : 1 ,
                       "exp" : 4 ,
                       "gold" : 3 ,
                       "item" : "goo" } ,

             "imp" : { "name" : "imp" ,
                       "maxhp" : 7 ,
                       "currhp" : 7 ,
                       "strength" : 6 ,
                       "defense" : 2 ,
                       "agility" : 2 ,
                       "exp" : 7 ,
                       "gold" : 4 ,
                       "item" : "imp hat" } ,

             "bat" : { "name" : "bat" ,
                       "maxhp" : 5 ,
                       "currhp" : 5 ,
                       "strength" : 2 ,
                       "defense" : 1 ,
                       "agility" : 4 ,
                       "exp" : 6 ,
                       "gold" : 3 ,
                       "item" : "broken wing" } ,

             "goblin" : { "name" : "goblin" ,
                       "maxhp" : 15 ,
                       "currhp" : 15 ,
                       "strength" : 8 ,
                       "defense" : 4 ,
                       "agility" : 5 ,
                       "exp" : 20 ,
                       "gold" : 8 ,
                       "item" : "goblin cap" } ,

             "boss" : { "name" : "boss" ,
                       "maxhp" : 20 ,
                       "currhp" : 20 ,
                       "strength" : 10 ,
                       "defense" : 5 ,
                       "agility" : 5 ,
                       "exp" : 50 ,
                       "gold" : 20 ,
                       "item" : "trophy" } ,

             "monster" : { "name" : "monster" ,
                       "maxhp" : 15 ,
                       "currhp" : 15 ,
                       "strength" : 3 ,
                       "defense" : 2 ,
                       "agility" : 2 ,
                       "exp" : 5 ,
                       "gold" : 1 ,
                       "item" : "item" } }

player = { 1 : { "name" : "Hero" ,
                 "maxhp" : 10 ,
                 "currhp" : 10 ,
                 "strength" : 5 ,
                 "defense" : 2 ,
                 "agility" : 4 ,
                 "luck" : 2 ,
                 "exp" : 0 ,
                 "next" : 10 ,
                 "level" : 1 ,
                 "gold" : 0 ,
                 "weapon" : "none",
                 "helm" : "none",
                 "armor" : "none",
                 "acc" : "none" } ,
           
           2 : { "name" : "Sidekick" ,
                 "maxhp" : 9 ,
                 "currhp" : 9 ,
                 "strength" : 3 ,
                 "defense" : 6 ,
                 "agility" : 3 ,
                 "luck" : 1 ,
                 "exp" : 0 ,
                 "next" : 10 ,
                 "level" : 1 ,
                 "gold" : 0 ,
                 "weapon" : "none",
                 "helm" : "none",
                 "armor" : "none",
                 "acc" : "none" } ,

           3 : { "name" : "Apprentice" ,
                 "maxhp" : 5 ,
                 "currhp" : 5 ,
                 "strength" : 1 ,
                 "defense" : 2 ,
                 "agility" : 6 ,
                 "luck" : 1 ,
                 "exp" : 0 ,
                 "next" : 10 ,
                 "level" : 1 ,
                 "gold" : 0 ,
                 "weapon" : "none",
                 "helm" : "none",
                 "armor" : "none",
                 "acc" : "none" } }

story = { 1 : { 1 : { 1 : "Text" ,
                    2 : "Text" ,
                    3 : "Test" ,
                    "switch" : 0 } ,

                2 : { "story" : "Text2" ,
                      "story2" : "Text2" ,
                      "story3" : "Text2" ,
                      "switch" : 0 } } ,

          2 : { 1 : { "story" : "Text" ,
                    "story2" : "Text" ,
                    "story3" : "Test" ,
                    "switch" : 0 } ,

                2 : { "story" : "Text2" ,
                      "story2" : "Text2" ,
                      "story3" : "Text2" ,
                      "switch" : 0 } } }

#Initialize
currentRoom = 1

showInstructions()

#main loop
while True:
    showStatus()
    
    move = input(">").split()
    print("\n")
    print("\n")
    print("\n")
    #catch if nothing is entered.
    if len(move) == 0:
        print("Please enter a valid command.")
    #========= go =========
    elif move[0] == "go":
        #catch if only go is entered.
        if len(move) == 1:
            print("Please specify where to go.")
        #catch if direction not allowed
        elif move[1] not in rooms[currentRoom]:
            print("You can't go that way.")
        #catch if door is locked
        elif rooms[currentRoom][move[1]] == "lock":
            print("The door is locked.")
        #catch if going up or down to a new floor
        elif move[1] == "up" or move[1] == "down":
            if rooms[currentRoom][move[1]] is not int:
                #save curent floor to retain object permanence
                previousfloor = "temp" + rooms[0]["name"]
                saveRooms(previousfloor,rooms)
                #load next floor
                nextfloor = "temp" + rooms[currentRoom][move[1]]
                #try:
                    #rooms = loadRooms(nextfloor)
                    #pass
                #except:
                    #print("No temp file.")
                    #pass
                #try:
                    #rooms = loadRooms(rooms[currentRoom][move[1]])
                    #pass
                #except:
                    #print("Load failed.")
                    #print(currentRoom)
                    #pass
                if path.exists(nextfloor + ".pkl"):
                    print("Temp exists!")
                    #load saved instance of floor
                    rooms = loadRooms(nextfloor)
                else:
                    print("Temp doesn't exist...")
                    #load original floor
                    rooms = loadRooms(rooms[currentRoom][move[1]])
        #move direction
        elif move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
    #========= take =========
    elif move[0] == "take":
        #catch if only take is entered.
        if len(move) == 1:
            print("Please specify what to take.")
        #take the item
        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            inventory += [move[1]]
            print("You picked up a " + move[1] + "!")
            del rooms[currentRoom]["item"]
        #take dropped item
        #elif "dropped" in rooms[currentRoom]:
        #    length = len(rooms[currentRoom]["dropped"])
        #    for item in rooms[currentRoom]["dropped"]:
        #        if move[1] in rooms[currentRoom]["dropped"][item]:
        #            inventory += [move[1]]
        #            print("You picked up a " + str(rooms[currentRoom]["dropped"][item][item]) + " that was dropped!")
        #    del rooms[currentRoom]["dropped"][length-1][item]
        elif "dropped" in rooms[currentRoom]:
            if move[1] in rooms[currentRoom]["dropped"]:
                inventory += [move[1]]
                print("You picked up a " + move[1] + "!")
                del rooms[currentRoom]["dropped"]
        #catch if item is not in room
        else:
            print("There is no " + move[1] + " here!")
    #========= use =========
    elif move[0] == "use":
        #catch if only use is entered.
        if len(move) == 1:
            print("Please specify what to use.")
        #catch if item not in inventory.
        elif move[1] not in inventory:
            print("You do not have a " + move[1])
        #catch if direction not specified.
        elif len(move) == 2:
            print("Please specify where or what to use the " + move[1] + " on.")
        #use item
        elif move[1] in inventory and move[2] in rooms[currentRoom]:
            #use key
            if move[1] == "key":
                #catch if no direction is given
                if len(move) < 2:
                    print("Please specify where to use the key.")
                #check if door is locked
                if rooms[currentRoom][move[2]] == "lock":
                    print("The door unlocks.")
                    #change lock into door that links to next room
                    if move[2] == "east":
                        rooms[currentRoom][move[2]] = currentRoom + 1
                    if move[2] == "west":
                        rooms[currentRoom][move[2]] = currentRoom - 1
                    if move[2] == "north":
                        rooms[currentRoom][move[2]] = currentRoom - 5
                    if move[2] == "south":
                        rooms[currentRoom][move[2]] = currentRoom + 5
                    #use up key
                    inventory.remove("key")
                #door is not locked
                else:
                    print("That door isn't locked.")
            #direction is not valid for item
            else:
                print("You can't use the " + move[1] + " in that direction.")
        #use potion
        elif move[1] == "potion":
            #catch if no target is given
            if len(move) < 2:
                print("Please specify who will drink the potion.")
            #check if target is a valid party member
            if searchDict(player, move[2]):
                print("That is not a party member!\n")
            else:
                healPlayer(move[2])
        #item is not usable
        else:
            print("You can't do that.")
    #========= fight =========
    elif move[0] == "fight":
        #catch if only fight is entered.
        if len(move) == 1:
            print("Please specify what to fight.")
        #catch if monster not in room.
        #elif move[1] not in rooms[currentRoom]:
         #   print("There's no " + move[1] + " monster here.")
        #fight monster
        #elif move[1] == rooms[currentRoom]["monster"]:
         #   battleStart(currentRoom, rooms[currentRoom]["monster"])
        elif "monster" in rooms[currentRoom] and move[1] in rooms[currentRoom]["monster"]:
            battleStart(currentRoom, rooms[currentRoom]["monster"])
        #catch if no monster in the room
        else:
            print("There's no " + move[1] + " monster here.")
    #========= kill =========
    elif move[0] == "kill":
        #catch if only command is entered.
        if len(move) == 1:
            print("Please specify what to kill.")
        #kill self
        elif move[1] == "self":
            print("Suicide is not the answer.")
        #kill party members
        elif move[1] not in player:
                print("You can't kill " + move[1])            
        else:
            for i in player:
                if move[1] == player[i]["name"]:
                    print("It's not nice to kill " + player[i]["name"])
    #========= read =========
    elif move[0] == "read":
        #catch if only command is entered.
        if len(move) == 1:
            print("Please specify what to read.")
        #read sign
        elif move[1] == "sign":
            #check if sign exists
            if move[1] in rooms[currentRoom]:
                print(rooms[currentRoom][move[1]])
                print("")
            else:
                print("There is no sign here.")
        else:
            print("There is nothing to read.")
    #========= save =========
    elif move[0] == "save":
        #catch if only command is entered.
        if len(move) == 1:
            saveGame()
            saveInventory()
            rpgrooms = "rpgrooms"
            saveRooms(rpgrooms,rooms)
    #command is not valid
    #========= load =========
    elif move[0] == "load":
        #catch if only command is entered.
        if len(move) == 1:
            player = loadGame(player)
            inventory = loadInventory(inventory)
            print("Final load: ")
            print(player)
            currentRoom = loadCurrentRoom("currentroom.pkl")
            rooms = loadRooms("rpgrooms") 
    #command is not valid
    #========= loadroom =========
    elif move[0] == "loadroom":
        #catch if only command is entered.
        if len(move) == 1:
            print("Load which rooms?")
        else:
            #load the new rooms
            rooms = loadRooms(move[1])
            print("Final load: ")
            print(rooms)
    #command is not valid
    #========= status =========
    elif move[0] == "status":
        battleStatus()
    #========= map =========
    elif move[0] == "map":
        showMap()
    #========= drop =========
    elif move[0] == "drop":
        #catch if only drop is entered.
        if len(move) == 1:
            print("Please specify what to drop.")
        #check length of item
        elif len(move) == 3:
            item = move[1] + " " + move[2]
            #catch if item is not in inventory
            if item not in inventory:
                print("You don't have " + item + " to drop.")
            elif item not in droppable:
                print("You can't drop " + item + "!")
            else:
                #check if room already has a dropped item
                if "dropped" in rooms[currentRoom]:
                    print("Room can only hold one dropped item.")
                else:
                    inventory.remove(item)
                    print("You dropped " + item + "!")
                    #add dropped item to current room
                    rooms[currentRoom]["dropped"] = item
        elif len(move) == 2:
            item = move[1]
            #catch if item is not in inventory
            if item not in inventory:
                print("You don't have " + item + " to drop.")
                #catch if item is not droppable
            elif item not in droppable:
                print("You can't drop " + item + "!")
            else:
                #check if room already has a dropped item
                if "dropped" in rooms[currentRoom]:
                    #length = len(rooms[currentRoom]["dropped"])
                    #rooms[currentRoom]["dropped"] = {length : [item]}
                    print("Room can only hold one dropped item.")
                else:
                    inventory.remove(item)
                    print("You dropped " + item)
                    #add dropped item to current room
                    rooms[currentRoom]["dropped"] = item
                    #else:
                        #length = 0
                        #rooms[currentRoom]["dropped"] = {length : [item]}
        else:
            print("Please enter a valid item to drop!")
    #========= equip =========
    elif move[0] == "equip":
        #catch if only command is entered.
        if len(move) == 1:
            print("Please specify what to equip.")
        #check length of item
        elif len(move) == 3:
            item = move[1] + " " + move[2]
        else:
            item = move[1]
        #catch if item is not in inventory
        if item not in inventory:
            print("You don't have " + item + " to equip.")
        #catch if player not specified.
        if len(move) == 4:
            print("Equip for who?")
        #command is not valid
    #========= look =========
    elif move[0] == "look":
        print(rooms[currentRoom]["init"])
    #========= new command =========
    elif move[0] == "command":
        #catch if only command is entered.
        if len(move) == 1:
            print("Please specify what to command.")
        #other cases
    #command is not valid
    else:
        print("You can't " + str(move))
        print("Please enter a valid command.")
        

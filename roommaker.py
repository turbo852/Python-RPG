#Room Maker

import string, random, pickle

def loadRooms(filename):
    #create filename string
    newRooms = str(filename) + ".pkl"
    print("Rooms: ")
    print(newRooms)
    fi = open(newRooms, "rb")
    tempRooms = pickle.load(fi)
    print("New rooms loaded successfully!")
    return  tempRooms

def saveRooms(filename,roomSet):
    print(filename)
    print(roomSet)
    #create filename string
    newRooms = str(filename) + ".pkl"
    fi = open(newRooms, "bw")
    pickle.dump(roomSet,fi)
    fi.close()
    print("Rooms saved!")

rooms = { 1 : { "name" : "Room1" ,
                "east" : 2 ,
                "south" : 6} ,
          
          2 : { "name" : "Room2" ,
                "west" : 1 ,
                "south" : 7 ,
                "item" : "sword" ,
                "east" : 3 } ,
          
          6 : { "name" : "Room3" ,
                "north" : 1 ,
                "monster" : "imp" ,
                "item" : "cookie" } ,
          
          7 : { "name" : "Room4" ,
                "north" : 2 ,
                "monster" : "slime" ,
                "item" : "key" } ,
          
          3 : { "name" : "Room5" ,
                "west" : 2 ,
                "east" : "lock" ,
                "item" : "key" } ,

          4 : { "name" : "Room6" ,
                "west" : 3 ,
                "east" : 5 ,
                "item" : "key" },
          
          5 : { "name" : "Room7" ,
                "west" : 4 ,
                "south" : 10 ,
                "item" : "potion" },
          
          10 : { "name" : "Room8" ,
                "north" : 5 ,
                "monster" : "bat" ,
                "item" : "coin" } }

rooms2 = { 1 : { "name" : "Room0" ,
                "east" : 2 ,
                "south" : 6 } ,
          
          2 : { "name" : "Room1" ,
                "west" : 1 ,
                "east" : 3 ,
                "item" : "sword" ,
                "monster" : "goblin" } ,
           
           3 : { "name" : "Room3" ,
                 "west" : 2 ,
                 "south" : 8 ,
                 "monster" : "imp"} ,

           6 : { "name" : "Room6" ,
                 "north" : 1 ,
                 "east" : 7 , } ,

           7 : { "name" : "Room7" ,
                 "north" : 2 ,
                 "east" : 8 ,
                 "west" : 6 } ,

           8 : { "name" : "Room8" ,
                 "north" : 3 ,
                 "west" : 7 } }
           

rooms3 = { 1 : { "name" : "Start" ,
                "east" : 2 ,
                "south" : 6} ,
          
          2 : { "name" : "Middle" ,
                "west" : 1 ,
                "south" : 7 ,
                "item" : "sign" ,
                "east" : 3 } ,

          3 : { "name" :  "End" ,
                "up" : 0 ,
                "item" : "key" ,
                "monster" : "boss" } }



floor1 = { 1 : { "name" : "Room1" ,
                "south" : 6} ,
          
          5 : { "name" : "Room5" ,
                "south" : 10 ,
                "up" : "floor2" } ,
          
          6 : { "name" : "Room6" ,
                "north" : 1 ,
                "south" : 11 ,
                "monster" : "imp" } ,
          
          8 : { "name" : "Room8" ,
                "south" : 13 ,
                "monster" : "slime" ,
                "item" : "key" } ,
          
          10 : { "name" : "Room10" ,
                "north" : 5 ,
                "south" : 15 ,
                "item" : "key" } ,

          11 : { "name" : "Room11" ,
                "north" : 6 ,
                "east" : 12 } ,
          
          12 : { "name" : "Room12" ,
                "west" : 11 ,
                "east" : 13 ,
                "item" : "potion" } ,
          
          13 : { "name" : "Start" ,
                "north" : 8 ,
                "west" : 12 ,
                "east" : "lock" ,
                "south" : 18 } ,

          14 : { "name" : "Room14" ,
                "west" : 13 ,
                "east" : 15 } ,
            
          15 : { "name" : "Room15" ,
                "north" : 10 ,
                "west" : 14 ,
                "item" : "potion" } ,
           
          18 : { "name" : "Room18" ,
                "north" : 13 ,
                "south" : 23 } ,
           
          21 : { "name" : "Room21" ,
                "east" : 22 ,
                "monster" : "goblin" } ,
           
          22 : { "name" : "Room22" ,
                "west" : 21 ,
                "east" : 23 } ,
           
          23 : { "name" : "Room23" ,
                "north" : 18 ,
                "west" : 22 ,
                "east" : 24 ,
                "monster" : "bat" } ,
           
          24 : { "name" : "Room24" ,
                "west" : 23 ,
                "monster" : "slime" ,
                "item" : "potion" } }

floor2 = { 3 : { "name" : "Room3" ,
                "south" : 8 ,
                "monster" : "goblin" } ,
          
          5 : { "name" : "Room5" ,
                "south" : 10 ,
                "down" : "floor1" } ,
          
          6 : { "name" : "Room6" ,
                "east" : 7 ,
                "south" : 11 ,
                "monster" : "imp" } ,

          7 : { "name" : "Room7" ,
                "west" : 6 ,
                "east" : 8 } ,
          
          8 : { "name" : "Room8" ,
                "north" : 3 ,
                "west" : 7 ,
                "south" : 13 } ,
          
          10 : { "name" : "Room10" ,
                "north" : 5 ,
                "south" : 15 } ,

          11 : { "name" : "Room11" ,
                "north" : 6 ,
                "south" : 16 } ,
          
          13 : { "name" : "Room13" ,
                "north" : 8 ,
                "monster" : "imp" } ,
            
          15 : { "name" : "Room15" ,
                "north" : 10 ,
                "south" : 20 ,
                "item" : "potion" } ,
           
          16 : { "name" : "Room16" ,
                "north" : 11 ,
                "south" : 21 } ,
                      
          18 : { "name" : "Room18" ,
                "south" : 23 ,
                "item" : "potion" } ,
                      
          20 : { "name" : "Room20" ,
                "north" : 15 ,
                "south" : 25 } ,
           
          21 : { "name" : "Room21" ,
                 "north" : 16 ,
                "east" : 22 } ,
           
          22 : { "name" : "Room22" ,
                "west" : 21 ,
                "east" : 23 } ,
           
          23 : { "name" : "Room23" ,
                "north" : 18 ,
                "west" : 22 ,
                "east" : 24 ,
                "monster" : "bat" } ,
           
          24 : { "name" : "Room24" ,
                "west" : 23 ,
                "east" : 25 } ,

          25 : { "name" : "Room25" ,
                "west" : 24 ,
                "north" : 20 ,
                "monster" : "slime" ,
                "item" : "potion" } }

testroom = { 1 : { "name" : "Start" ,
                "item" : "potion" ,
                "east" : 2 ,
                "south" : 6 } ,
          
          2 : { "name" : "2" ,
                "west" : 1 ,
                "item" : "key" ,
                "east" : 3 } ,

          3 : { "name" :  "3" ,
                "item" : "key" ,
                "monster" : "blob" ,
                "east" : 4 } ,

          4 : { "name" : "4" ,
                "west" : 3 ,
                "item" : "potion"  ,
                "monster" : "slime" ,
                "east" : 5 } ,

          5 : { "name" : "5" ,
                "west" : 4 ,
                "item" : "potion"  ,
                "monster" : "imp" ,
                "south" : 5 } ,

          6 : { "name" :  "6" ,
                "north" : 1 ,
                "monster" : "imp" ,
                "east" : 7 } 
             }
          


rpgf1 = { 0 : { "name" : "rpgf1" } ,

          1 : { "name" : "the Start" ,
                "init" : "You see yourself in a very plain but dusty room." ,
                "initSwitch" : "on" ,
                "east" : 2 ,
                "south" : 6 ,
                "sign" : "This is the start." } ,

          2 : { "name" : "Room 2" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "east" : 3 ,
                "up" : "rpgf2" } ,

          3 : { "name" : "Room 3" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "west" : 2 ,
                "south" : 8 } ,

          4 : { "name" : "Room 4" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "east" : 5 ,
                "up" : "rpgf2" } ,
          
          5 : { "name" : "Room 5" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "west" : 4 ,
                "south" : 10 } ,
          
          6 : { "name" : "Room 6" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "north" : 1 ,
                "south" : 11 } ,

          8 : { "name" : "Room 8" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "north" : 3 ,
                "south" : 13 } ,

          9 : { "name" : "Room 9" ,
                "init" : "A plain basic room" ,
                "initSwitch" : "on" ,
                "east" : 10 ,
                "south" : 14 } ,
          
          10 : { "name" : "Room 10" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : "lock" ,
                 "west" : 9 ,
                 "monster" : "bat" } ,
          
          11 : { "name" : "Room 11" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 6 ,
                 "east" : 12 ,
                 "monster" : "blob" } ,

          12 : { "name" : "Room 12" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "west" : 11 ,
                  "east" : "lock" ,
                 "south" : 17 ,
                 "item" : "potion" } ,

          13 : { "name" : "Room 13" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 8 ,
                 "west" : 12 ,
                 "east" : 14 ,
                 "monster" : "slime" } ,

          14 : { "name" : "Room 14" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 9 ,
                 "west" : 13 ,
                 "south" : 19 } ,

          17 : { "name" : "Room 17" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 12 ,
                 "south" : 22 } ,

          19 : { "name" : "Room 19" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 14 ,
                 "item" : "potion" } ,

          20 : { "name" : "Room 20" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "up" : "rpgf2" ,
                 "south" : 25 } ,

          21 : { "name" : "Room 21" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "east" : 22 ,
                 "item" : "key" } ,

          22 : { "name" : "Room 22" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 17 ,
                 "west" : 21 ,
                 "monster" : "slime" } ,

          25 : { "name" : "Room 25" ,
                 "init" : "A plain basic room" ,
                 "initSwitch" : "on" ,
                 "north" : 20 ,
                 "item" : "key" } }



rpgf2 = { 0 : { "name" : "rpgf2" } ,

          2 : { "name" : "Room 2" ,
                "south" : 7 ,
                "down" : "rpgf1" } ,

          4 : { "name" : "Room 4" ,
                "east" : 5 ,
                "down" : "rpgf1" } ,
          
          5 : { "name" : "Room 5" ,
                "west" : 4 ,
                "south" : 10 } ,
          
          6 : { "name" : "Room 6" ,
                "east" : 7 ,
                "south" : 11 ,
                "monster" : "imp" } ,

          7 : { "name" : "Room 7" ,
                "north" : 2 ,
                "west" : 6 } ,

          8 : { "name" : "Room 8" ,
                "south" : 13 ,
                "item" : "potion" } ,

          10 : { "name" : "Room 10" ,
                "north" : 5 ,
                "up" : "rpgf3" } ,
          
          11 : { "name" : "Room 11" ,
                "north" : 6 ,
                "south" : 16 } ,

          13 : { "name" : "Room 13" ,
                "north" : 8 ,
                "south" : 18 ,
                "monster" : "imp"} ,

          14 : { "name" : "Room 14" ,
                "south" : 19 } ,

          16 : { "name" : "Room 16" ,
                "north" : 11 ,
                "east" : 17 } ,

          17 : { "name" : "Room 17" ,
                "west" : 16 ,
                "east" : 18 } ,

          18 : { "name" : "Room 18" ,
                "west" : 17 ,
                "north" : 13 ,
                "east" : 19 } ,

          19 : { "name" : "Room 19" ,
                "east" : 20 ,
                "north" : 14 ,
                "west" : 18 ,
                "south" : 24 } ,

          20 : { "name" : "Room 20" ,
                "west" : 19 ,
                "down" : "rpgf1" } ,

          21 : { "name" : "Room 21" ,
                "east" : 22 ,
                "item" : "sword" } ,

          22 : { "name" : "Room 22" ,
                "west" : 21 ,
                "up" : "rpgf3" } ,

          24 : { "name" : "Room 24" ,
                "north" : 19 ,
                "item" : "potion" } ,
          
          }



rpgf3 = { 0 : { "name" : "rpgf3" } ,

          1 : { "name" : "Room 1" ,
                "south" : 6 ,
                "east" : 2 } ,

          2 : { "name" : "Room 2" ,
                "east" : 3 ,
                "west" : 1 ,
                "monster" : "imp" } ,

          3 : { "name" : "Room 3" ,
                "east" : 4 ,
                "west" : 2 } ,

          4 : { "name" : "Room 4" ,
                "east" : 5 ,
                "west" : 3 } ,
          
          5 : { "name" : "Room 5" ,
                "west" : 4 ,
                "south" : 10 ,
                "monster" : "slime" } ,
          
          6 : { "name" : "Room 6" ,
                "south" : 11 ,
                "north" : 1 ,
                "monster" : "bat" } ,

          8 : { "name" : "Room 8" ,
                "east" : 9 ,
                "south" : 13 ,
                "item" : "key" } ,

          9 : { "name" : "Room 9" ,
                "east" : 10 ,
                "west" : 8 } ,
          
          10 : { "name" : "Room 10" ,
                "north" : 5 ,
                "west" : "lock" ,
                "south" : 15 ,
                "down" : "rpgf2" } ,
          
          11 : { "name" : "Room 11" ,
                "north" : 6 ,
                "east" : "lock" ,
                "south" : 16 } ,

          12 : { "name" : "Room 12" ,
                "west" : 11 ,
                "east" : 13 } ,

          13 : { "name" : "Room 13" ,
                "north" : 8 ,
                "west" : 12 ,
                "item" : "key" } ,

          15 : { "name" : "Room 15" ,
                "north" : 10 ,
                "south" : 20 } ,

          16 : { "name" : "Room 16" ,
                "north" : 11 ,
                "monster" : "goblin" ,
                "south" : 21 } ,

          18 : { "name" : "Room 18" ,
                "south" : 23 ,
                "item" : "potion" } ,

          19 : { "name" : "Room 19" ,
                "east" : 20 ,
                "item" : "potion" } ,

          20 : { "name" : "Room 20" ,
                "north" : 15 ,
                "west" : 19 ,
                "south" : 25 } ,

          21 : { "name" : "Room 21" ,
                "north" : 16 ,
                "item" : "key" } ,

          22 : { "name" : "Room 22" ,
                "east" : 23 ,
                "down" : "rpgf2" } ,

          23 : { "name" : "Room 23" ,
                "north" : 18 ,
                "east" : 24 ,
                 "west" : 22 ,
                "monster" : "imp" } ,

          24 : { "name" : "Room 24" ,
                "east" : 25 ,
                "west" : "lock" } ,

          25 : { "name" : "Room 25" ,
                "north" : 20 ,
                "west" : 24 ,
                "monster" : "imp" } ,
          }



allrooms = [rooms, rooms2, rooms3]

newRooms = {}

#main loop
while True:
    move = input(">").split()
    print("\n")
    print("\n")
    print("\n")
    #catch if nothing is entered.
    if len(move) == 0:
        print("Please enter a valid command.")
    #========= loadroom =========
    elif move[0] == "loadroom":
        #catch if only command is entered.
        if len(move) == 1:
            print("Load which rooms?")
        else:
            newRooms = loadRooms(move[1])
            print("Final load: ")
            print(newRooms)
    #========= saveroom =========
    elif move[0] == "saveroom":
        #catch if only command is entered.
        if len(move) == 1:
            print("Save which rooms? Please supply a filename and which roomset to save.")
        elif len(move) == 2:
            print("Save which roomset? Please supply a filename and which roomset to save.")
        elif len(move) == 3:
            #for item in allrooms:
            #    if move[2] == item:
            #        move[2] = allrooms[item-1]
            if move[2] == "rooms":
               move[2] = rooms
            elif move[2] == "rooms2":
               move[2] = rooms2
            elif move[2] == "rooms3":
                move[2] = rooms3
            elif move[2] == "floor1":
                move[2] = floor1
            elif move[2] == "floor2":
                move[2] = floor2
            elif move[2] == "testroom":
                move[2] = testroom
            elif move[2] == "rpgf1":
                move[2] = rpgf1
            elif move[2] == "rpgf2":
                move[2] = rpgf2
            elif move[2] == "rpgf3":
                move[2] = rpgf3
            saveRooms(move[1],move[2])
            print("Rooms saved as: ")
            print(move[1])
        else:
            print("Please supply a filename and which roomset to save.")
    #========= printroom =========
    elif move[0] == "printroom":
        print(newRooms)
    #command is not valid
    else:
        print("You can't " + str(move))
        print("Please enter a valid command.")

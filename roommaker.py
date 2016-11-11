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
            print("Save which rooms?")
        elif len(move) == 2:
            print("Save which roomset?")
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

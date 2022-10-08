import random
import keyboard

class Data:
    character_Position = [25,6]  #    x , y
    wallLocations = []
    
    ScreenSize = [50,14]
    
    totalScore = 0
    diffcultlyLevel = 0
    runningGame =  True
    
    # Train Data
    trains = []
    
    trainLocations_T = []
    trainLocations_R = []
    trainLocations_B = []
    trainLocations_L = []

def draw_screen():
    
    print("\n"*5)
    print("-"*51)
    
    for y_ in range(1, Data.ScreenSize[1]):
        row = "|"
        for x_ in range(1, Data.ScreenSize[0]):
            
            cell_Location = [x_, y_]
            
            if (Data.character_Position in Data.trainLocations_T or 
                Data.character_Position in Data.trainLocations_R or 
                Data.character_Position in Data.trainLocations_B or 
                Data.character_Position in Data.trainLocations_L):
                
                if Data.diffcultlyLevel == 1:
                    d = "Normal"
                elif Data.diffcultlyLevel == 2:
                    d = "Hard"
                else:
                    d = "Master"
                
                print(" ")
                print("DEATH")
                print("Diffculty: " + d)
                print("Score: " + str(Data.totalScore))
                print(" ")
                print("-"*50)
                Data.runningGame = False
                return
            
            if Data.character_Position == cell_Location:
                row += "X"
            elif cell_Location in Data.trainLocations_T:
                if Data.diffcultlyLevel == 3:
                    row += "|"
                else:
                    row += "v"
            elif cell_Location in Data.trainLocations_R:
                if Data.diffcultlyLevel == 3:
                    row += "="
                else:
                    row += "<"
            elif cell_Location in Data.trainLocations_B:
                if Data.diffcultlyLevel == 3:
                    row += "|"
                else:
                    row += "^"
            elif cell_Location in Data.trainLocations_L:
                if Data.diffcultlyLevel == 3:
                    row += "="
                else:
                    row += ">"
            elif cell_Location in Data.wallLocations:
                row += "+"
            else:
                row += " "
        print(row + "|")
    
    print("-"*50)
    print(" ")
    
def start():
    
    print("")
    print("████████╗██████╗░░█████╗░██╗███╗░░██╗  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░ \n" +
          "╚══██╔══╝██╔══██╗██╔══██╗██║████╗░██║  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░ \n" +
          "░░░██║░░░██████╔╝███████║██║██╔██╗██║  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░ \n" +
          "░░░██║░░░██╔══██╗██╔══██║██║██║╚████║  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░ \n" +
          "░░░██║░░░██║░░██║██║░░██║██║██║░╚███║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗ \n" +
          "░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝")
    print("")
    print("How to play: \n Move with the 'ASWD' Keys to dodge the moving Trains(^<v>) \n with the the (+) wall growing")
    
    while Data.diffcultlyLevel == 0:
        print("\n")
        print("1: Normal")
        print("2: Hard")
        print("3: Master")
        print(" ")
        diffcultly = input("Choose the diffcutly level: ")
        try:
            Data.diffcultlyLevel = int(diffcultly)
        except:
            pass
        
    random_WallGrowth()
    draw_screen()
    
    keyboard.on_press_key('w', lambda e: moveUP(e), suppress=True)
    keyboard.on_press_key('s', lambda e: moveDown(e), suppress=True)
    keyboard.on_press_key('a', lambda e: moveLeft(e), suppress=True)
    keyboard.on_press_key('d', lambda e: moveRight(e), suppress=True)
    
    while Data.runningGame:
        if keyboard.is_pressed('f'):
            print("Exiting Game...")
            break
        
def moveUP(e):
    
    if (Data.character_Position[1] - 1) <= 0:
        return
    
    pre = [Data.character_Position[0], Data.character_Position[1] - 1]
    if pre in Data.wallLocations:
        return
    
    spawnTrain()
    
    trainMovement()
    random_WallGrowth()
    
    _y = Data.character_Position[1]
    Data.character_Position = [Data.character_Position[0], _y - 1]
    draw_screen()
    
    Data.totalScore += 1
    
def moveDown(e):
    
    if (Data.character_Position[1] + 1) >= Data.ScreenSize[1]:
        return
    
    pre = [Data.character_Position[0], Data.character_Position[1] + 1]
    if pre in Data.wallLocations:
        return
    
    spawnTrain()
    
    trainMovement()
    random_WallGrowth()
    
    _y = Data.character_Position[1]
    Data.character_Position = [Data.character_Position[0], _y + 1]
    draw_screen()
    
    Data.totalScore += 1
    
def moveLeft(e):
    
    if (Data.character_Position[0] - 1) <= 0:
        return
    
    pre = [Data.character_Position[0] - 1, Data.character_Position[1]]
    if pre in Data.wallLocations:
        return
    
    spawnTrain()
    
    trainMovement()
    random_WallGrowth()
    
    _x = Data.character_Position[0]
    Data.character_Position = [_x - 1, Data.character_Position[1]]
    draw_screen()
    
    Data.totalScore += 1
    
def moveRight(e):
    
    if (Data.character_Position[0] + 1) >= Data.ScreenSize[0]:
        return
    
    pre = [Data.character_Position[0] + 1, Data.character_Position[1]]
    if pre in Data.wallLocations:
        return
    
    spawnTrain()
    
    trainMovement()
    random_WallGrowth()
    
    _x = Data.character_Position[0]
    Data.character_Position = [_x + 1, Data.character_Position[1]]
    draw_screen()
    
    Data.totalScore += 1
    
def trainMovement():
    Data.trainLocations_T.clear()
    Data.trainLocations_L.clear()
    Data.trainLocations_B.clear()
    Data.trainLocations_R.clear()
    
    newTrainSet = []
    
    for train in Data.trains:
        if train[0] == "T":
            for b in range(0, train[1]):
                G = [train[2], (train[3]-b)]
                Data.trainLocations_T.append(G)
            
            newpos = (train[3] + 1)
            if newpos < (Data.ScreenSize[1] + train[1] + 2):
                U = [train[0], train[1], train[2], newpos]
                newTrainSet.append(U)
            
        if train[0] == "R":
            for b in range(0, train[1]):
                G = [train[2]-b, train[3]]
                Data.trainLocations_R.append(G)
            
            newpos = (train[2] - 1)
            if newpos < (Data.ScreenSize[0] + train[1] + 2):
                U = [train[0], train[1], newpos, train[3]]
                newTrainSet.append(U)
            
        if train[0] == "B":
            for b in range(0, train[1]):
                G = [train[2], (train[3]+b)]
                Data.trainLocations_B.append(G)
                
            newpos = (train[3] - 1)
            if newpos < (Data.ScreenSize[1] + train[1] + 2):
                U = [train[0], train[1], train[2], newpos]
                newTrainSet.append(U)
            
        if train[0] == "L":
            for b in range(0, train[1]):
                G = [train[2]+b, train[3]]
                Data.trainLocations_L.append(G)
                
            newpos = (train[2]+1)
            if newpos < (Data.ScreenSize[0] + train[1] + 2):
                U = [train[0], train[1], newpos, train[3]]
                newTrainSet.append(U)
    
    Data.trains.clear()
    Data.trains = newTrainSet

def spawnTrain():
    
    if Data.diffcultlyLevel == 1:
        chance = random.randrange(1,4) # 33% chance to spawn Train
        if chance != 1:
            return
    elif Data.diffcultlyLevel == 2:
        chance = random.randrange(1,3) # %50 chance to spawn Train
        if chance != 1:
            return
       
    side = random.randrange(1,5)
    
    if side == 1: # top ^
        loc = [random.randrange(1, Data.ScreenSize[0]), 1]
        data_ = ["T", random.randrange(2,8), loc[0], loc[1]]  # side, size, head-x-position, head-y-position
        Data.trains.append(data_)
        Data.trainLocations_T.append(loc)
    elif side == 2: # right
        loc = [Data.ScreenSize[0], random.randrange(1, Data.ScreenSize[1])]
        data_ = ["R", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
        Data.trains.append(data_)
        Data.trainLocations_R.append(loc)
    elif side == 3: # bottom
        loc = [random.randrange(1, Data.ScreenSize[0]), Data.ScreenSize[1]]
        data_ = ["B", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
        Data.trains.append(data_)
        Data.trainLocations_R.append(loc)
    else: # left
        loc = [1, random.randrange(1, Data.ScreenSize[1])]
        data_ = ["L", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
        Data.trains.append(data_)
        Data.trainLocations_R.append(loc)
    
def random_WallGrowth():
    # pick starting pos
    
    if len(Data.wallLocations) == 0:
        newX = random.randrange(1,Data.ScreenSize[0])
        newy = random.randrange(1,Data.ScreenSize[1])
        Data.wallLocations.append([newX, newy])
    else:
        openSpots = []
        
        for L in Data.wallLocations:
            
            if L[0] >= 2:
                h = [(L[0]-1), L[1]]
                if h not in Data.wallLocations and h not in openSpots and h != Data.character_Position:
                    openSpots.append(h)
                    
            if L[0] < Data.ScreenSize[0]:
                h = [(L[0]+1), L[1]]
                if h not in Data.wallLocations and h not in openSpots and h != Data.character_Position:
                    openSpots.append(h)
                    
            if L[1] >= 2:
                h = [L[0], (L[1]-1)]
                if h not in Data.wallLocations and h not in openSpots and h != Data.character_Position:
                    openSpots.append(h)
                    
            if L[1] < Data.ScreenSize[1]:
                h = [L[0], (L[1]+1)]
                if h not in Data.wallLocations and h not in openSpots and h != Data.character_Position:
                    openSpots.append(h)
            
        randomPick = random.randrange(0, len(openSpots))
        Data.wallLocations.append(openSpots[randomPick])
        
start()
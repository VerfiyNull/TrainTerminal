import random
import keyboard

class Data:
    character_Position = [25,6]  #    x , y
    wallLocations = []
    
    ScreenSize = [50,14]
    
    totalScore = 0
    Levels = ["Normal", "Hard", "Master"]
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
                
                print(" ")
                print("DEATH")
                print(f"Diffculty: {Data.Levels[Data.diffcultlyLevel-1]}")
                print(f"Score: {str(Data.totalScore)}")
                print(" ")
                print("-"*50)
                Data.runningGame = False
                return
            
            if Data.character_Position == cell_Location:
                row += "X"
            elif cell_Location in Data.trainLocations_T:
                row += "|" if Data.diffcultlyLevel == 3 else "v"
            elif cell_Location in Data.trainLocations_R:
                row += "=" if Data.diffcultlyLevel == 3 else "<"
            elif cell_Location in Data.trainLocations_B:
                row += "|" if Data.diffcultlyLevel == 3 else "^"
            elif cell_Location in Data.trainLocations_L:
                row += "=" if Data.diffcultlyLevel == 3 else ">"
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
        for i in range(0, len(Data.Levels)):
            print(f"Pick {i} - [ {Data.Levels[i]} ]")
        print("\n")
        diffcultly = input("Choose the diffcutly level: ")
        
        try:
            Data.diffcultlyLevel = int(diffcultly) if int(diffcultly) < 4 else 0
        except:
            pass
        
    random_WallGrowth()
    draw_screen()
    
    for key in ['w', 's', 'a', 'd']:
        keyboard.on_press_key(key, lambda e, d=key: moveSteps(e, d), suppress=True)
    
    while Data.runningGame:
        if keyboard.is_pressed('esc'):
            print("Exiting Game...")
            break

def moveSteps(e, d: str):

    match d:
        case "w":
            if (Data.character_Position[1] - 1) <= 0:
                return

            pre = [Data.character_Position[0], Data.character_Position[1] - 1]
            if pre in Data.wallLocations:
                return

            _y = Data.character_Position[1]
            Data.character_Position = [Data.character_Position[0], _y - 1]
        case "s":
            if (Data.character_Position[1] + 1) >= Data.ScreenSize[1]:
                return

            pre = [Data.character_Position[0], Data.character_Position[1] + 1]
            if pre in Data.wallLocations:
                return

            _y = Data.character_Position[1]
            Data.character_Position = [Data.character_Position[0], _y + 1]
        case "a":
            if (Data.character_Position[0] - 1) <= 0:
                return

            pre = [Data.character_Position[0] - 1, Data.character_Position[1]]
            if pre in Data.wallLocations:
                return

            _x = Data.character_Position[0]
            Data.character_Position = [_x - 1, Data.character_Position[1]]
        case "d":
            if (Data.character_Position[0] + 1) >= Data.ScreenSize[0]:
                return

            pre = [Data.character_Position[0] + 1, Data.character_Position[1]]
            if pre in Data.wallLocations:
                return
    
            _x = Data.character_Position[0]
            Data.character_Position = [_x + 1, Data.character_Position[1]]

    spawnTrain()
    trainMovement()
    random_WallGrowth()
    draw_screen()
    
    Data.totalScore += 1
    
def trainMovement():
    Data.trainLocations_T.clear()
    Data.trainLocations_L.clear()
    Data.trainLocations_B.clear()
    Data.trainLocations_R.clear()
    
    newTrainSet = []
    
    for train in Data.trains:
        match train[0]:
            case "T":
                for b in range(0, train[1]):
                    G = [train[2], (train[3]-b)]
                    Data.trainLocations_T.append(G)

                newpos = (train[3] + 1)
                if newpos < (Data.ScreenSize[1] + train[1] + 2):
                    U = [train[0], train[1], train[2], newpos]
                    newTrainSet.append(U)
            case "R":
                for b in range(0, train[1]):
                    G = [train[2]-b, train[3]]
                    Data.trainLocations_R.append(G)

                newpos = (train[2] - 1)
                if newpos < (Data.ScreenSize[0] + train[1] + 2):
                    U = [train[0], train[1], newpos, train[3]]
                    newTrainSet.append(U)
            case "B":
                for b in range(0, train[1]):
                    G = [train[2], (train[3]+b)]
                    Data.trainLocations_B.append(G)
                    
                newpos = (train[3] - 1)
                if newpos < (Data.ScreenSize[1] + train[1] + 2):
                    U = [train[0], train[1], train[2], newpos]
                    newTrainSet.append(U)
            
            case "L":
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
    
    chance = random.randrange(1,101)
    match Data.diffcultlyLevel:
        case 1:
            if chance > 66: # 33% chance to spawn Train
                return
        case 2:
            if chance > 50: # %50 chance to spawn Train
                return
            
    data_ = ""
    match (random.randrange(1,5)):
        case 1: # top ^
            loc = [random.randrange(1, Data.ScreenSize[0]), 1]
            data_ = ["T", random.randrange(2,8), loc[0], loc[1]]  # side, size, head-x-position, head-y-position
            Data.trainLocations_T.append(loc)
        case 2: # right
            loc = [Data.ScreenSize[0], random.randrange(1, Data.ScreenSize[1])]
            data_ = ["R", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
            Data.trainLocations_R.append(loc)
        case 3: # bottom
            loc = [random.randrange(1, Data.ScreenSize[0]), Data.ScreenSize[1]]
            data_ = ["B", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
            Data.trainLocations_B.append(loc)
        case _: # left
            loc = [1, random.randrange(1, Data.ScreenSize[1])]
            data_ = ["L", random.randrange(2,8), loc[0], loc[1]] # side, size, head-x-position, head-y-position
            Data.trainLocations_L.append(loc)
            
    Data.trains.append(data_)
    
def random_WallGrowth():
    # pick starting pos
    
    if len(Data.wallLocations) == 0:
        Data.wallLocations.append(
            [random.randrange(1,Data.ScreenSize[0]),
              random.randrange(1,Data.ScreenSize[1])])
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
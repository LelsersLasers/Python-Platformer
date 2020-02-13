import msvcrt
import os
import time

gameOn = True
x = 2 #change when i get GOOD screens
y = 3 #change when i get GOOD screens
score = 0
screen = 0
oldX = 0
oldY = 0
spawnX = 1
spawnY = 1
spawnScreen = 0
moveUp = 0
direction = ""
screen0 = ["###############", "#             #", "#>            #", "#>    r        ", "#>             ", "###############"]
screen1 = ["###############", "#             #", "#             #", "#>             ", "       r###    ", "###############"]
screen2 = ["###############", "#             #", "#      C      #", "#             #", "        ### rC#", "###############"]
screenList = [screen0, screen1, screen2]

def reset():
    global screenList
    for screenCount in range(0,len(screenList)):
        for yCount in range(0,len(screenList[screenCount])):
            for xCount in range(0, len((screenList[screen])[yCount])):
                if (list((screenList[screenCount])[yCount]))[xCount] == "c":
                    #print("yee")
                    a = list((screenList[screenCount])[yCount])
                    a[xCount] = "C"
                    (screenList[screenCount])[yCount] = "".join(a)
                    #(list((screenList[screenCount])[yCount]))[xCount] = "C"



def draw():
    #global screen0
    global screenList
    global x
    global oldX
    global y
    global oldY
    global score
    v = False
    if y != int(y):
        v = True
    y = int(y)
    os.system('cls')
    a = list((screenList[screen])[y])
    b = (screenList[screen])[y]
    a[x] = "0"
    (screenList[screen])[y] = "".join(a)
    print((screenList[screen])[0])
    print((screenList[screen])[1])
    print((screenList[screen])[2])
    print((screenList[screen])[3])
    print((screenList[screen])[4])
    print((screenList[screen])[5])
    (screenList[screen])[y] = b
    a = list((screenList[screen])[y])
    #sprint(a[x])
    if a[x] == "C":
        a[x] = "c"
        (screenList[screen])[y] = "".join(a)


    print("Score: " + str(score))
    if v:
        y = y + 0.5


def movement():
    #global screen0
    #global screen1
    global screenList
    global oldX
    global oldY
    global x
    global y
    global direction
    global moveUp
    v = False
    if y != int(y):
        v = True
    y = int(y)
    oldX = x
    oldY = y
    if msvcrt.kbhit():
        keyInput = msvcrt.getch().decode("utf-8").lower()
        direction = keyInput
    a = list((screenList[screen])[y+1])
    if direction == " " and a[x] == "#":
        moveUp = 5
    if direction == 'a':
        x = x - 1
    if direction == 'd':
        x = x + 1
    if moveUp > 0:
        moveUp = moveUp - 1
        y = y - 1
    if v:
        y = y + 0.5


def logic():
    #global screen0
    global screenList
    global y
    global x
    global spawnX
    global spawnY
    global screen
    global spawnScreen
    global direction
    global moveUp
    global score
    v = False
    if y != int(y):
        v = True
    y = int(y)
    a = list((screenList[screen])[y])
    if a[x] == "#":
        y = oldY
        x = oldX
    if a[x] == "r":
        spawnX = x
        spawnY = y
        spawnScreen = screen
        print("NEW SPAWN POINT")
    if a[x] == "C":
        score = score + 100
        print("POINT EARNED")
    if a[x] == "<" or a[x] == ">" or a[x] == "^":
        draw()
        x = spawnX
        y = spawnY
        screen = spawnScreen
        direction = ""
        reset()
        print("DEATH")
        time.sleep(0.5)
        score = 0
        moveUp = 0
    if x >= 14: #change when i get GOOD screens
        screen = screen + 1
        x = 1 #change when i get GOOD screens
        #y = 3 #change when i get GOOD screens
    if x <= 0:
        screen = screen - 1
        x = 13 #change when i get GOOD screens
    if v:
        y = y + 0.5

def startUp():
    print("g jkh j  ")

#(screenList[screen])[y+1]
def gravity():
    #global screen0
    global screenList
    global x
    global y
    global moveUp
    v = False
    b = 0
    if y != int(y):
        v = True
        b = y - int(y)
    y = int(y)
    if moveUp == 0:
        a = list((screenList[screen])[y+1])
        #print(a[x])
        if a[x] != "#":
            y = y + 0.5
    if v:
        y = y + 0.5


draw()
while gameOn:
    movement()
    gravity()
    logic()
    draw()
    #time.sleep(1)

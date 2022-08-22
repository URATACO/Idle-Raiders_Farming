import pyautogui as pyg
import time


#set game area
print('hit enter in terminal on top left of screen')
temp = input()
tl = pyg.position()
print('hit enter in terminal for bottom right of screen')
temp = input()
br = pyg.position()

gamescreen = (tl[0], tl[1], br[0]-tl[0], br[1]-tl[1])
gs = gamescreen

#red
red = (194, 0, 9)
#blue
#blue = ()
#green 
green = (0, 194, 32)
#yellow
yellow = (189, 196, 0)
acceptable = [red, green, yellow]
while True:
    print('reset')
    for x in range(gs[0],gs[0]+gs[2],10):
        for y in range(gs[1],gs[1]+gs[3],10):
            #pyg.moveTo(x,y)
            pix = pyg.pixel(x,y)
            
            #print('x: ' + str(x) , 'y: ' + str(y))
            #print(pix)
            for i in acceptable:
                #print(i)
                if pix == i:
                    print('found')
                    pyg.click(x,y)

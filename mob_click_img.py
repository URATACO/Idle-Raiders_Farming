from genericpath import isdir
import pyautogui as pyg
import cv2
import os
import time
import keyboard


pyg.PAUSE = 0.01

def file_chose():
    global file_folder
    print('If You Are Here Please Contact Dev To Update This Section')
        #file Directory
    file_folder = []
    dir_path = r"C:\Users\Drewt\OneDrive\Desktop\python\projects\idle raiders mob click\farm map img"
    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)):
            new_path = os.path.join(dir_path)
    for path in os.listdir(dir_path):
        new_path = os.path.join(dir_path, path)
        file_folder.append(new_path)
    # searching
    #print(file_folder)
            

def gamescreen_loc():
    global gs
    print('If You Are Here Please Contact Dev To Update This Section')
    #this section is not to be used yet
    time.sleep(500)
    #set game area
    print('hit enter in terminal on top left of screen')
    temp = input()
    tl = pyg.position()
    print('hit enter in terminal for bottom right of screen')
    temp = input()
    br = pyg.position()

    gamescreen = (tl[0], tl[1], br[0]-tl[0], br[1]-tl[1])
    gs = gamescreen


def raid_arena_mode():
    print('If You Are Here Please Contact Dev To Update This Section')

def farming_mode():
    print('If You Are Here Please Contact Dev To Update This Section')
    #this section is not to be used yet
    time.sleep(500)
    while keyboard.is_pressed('p') == False:
        for img in file_folder:
            loc = pyg.locateCenterOnScreen(img, region=gs, confidence=0.75)
            if loc != None:
                click_times = 12
                #print('Found enemy and attacking now')
                #print(loc)
                while click_times >= 0:
                    pyg.click(loc)
                    click_times -= 1
            else:
                #print('no enemy found')
                #time.sleep(1)
                continue 


# Main Terminal
def Main():
    
    print('What Would You Like To Do?')
    print('1: Check If Gamescreen Is Avalible')
    print('2: Enter Raid/Arena Mode')
    print('3: Enter Farming Mode')
    print('')
    print('')

    user_input = input()
    us = user_input
    if us == 1:
        if gs !=  None:
            print('Gamescreen Avalible')
            print('Is It Acceptable?')
            img = pyg.screenshot(region=gs)
            cv2.imshow('Gamescreen', img)
            cv2.waitKey(0)
            print('1: Yes')
            print('2: No')
            us = input()
            if us == 1:
                print('GameScreen Accepted')
            elif us ==2:
                print('Retaking GameScreen')
                print('If You Are Here Please Contact Dev To Update This Section') #yes im talking to myself since i'm the only one using this.
        else:
            print('Finding GameScreen')
            print('If You Are Here Please Contact Dev To Update This Section')
    elif us == 2:
        raid_arena_mode()
    elif us == 3:
        farming_mode()
    else:
        os.system('CLS')





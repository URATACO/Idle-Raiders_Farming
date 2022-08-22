import pyautogui as pyg
import cv2
import os
import time
import keyboard

pyg.PAUSE = 0.01
#set game area
print('hit enter in terminal on top left of screen')
temp = input()
tl = pyg.position()
print('hit enter in terminal for bottom right of screen')
temp = input()
br = pyg.position()

gamescreen = (tl[0], tl[1], br[0]-tl[0], br[1]-tl[1])
gs = gamescreen

#file path
file_folder = []
dir_path = r"C:\Users\Drewt\OneDrive\Desktop\python\projects\idle raiders mob click\farm map img\desert"
for path in os.listdir(dir_path):
    new_path = os.path.join(dir_path, path)
    file_folder.append(new_path)
# searching
#print(file_folder)
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



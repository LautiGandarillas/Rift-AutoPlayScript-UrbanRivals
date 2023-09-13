from pyautogui import *
import pyautogui
import time
import keyboard
import random
import movements # Calling movements

# Welcome to this early commit! Right now I'll be trying to play a flash piano-type game to test some things. Game's link: [https://www.silvergames.com/es/dont-touch-the-red]

# Ran [>>> pyautogui.displayMousePosition()] command on python's IDLE to obtain cords' x, y and RGB values.

#
#
#
#

# Green RGB value = (14, 208,  56)
# Red RGB value = (237,  28,  36)

#POS1: X:  920  Y: 240 RGB: (  14, 208,  56) 
#POS2: X:  1020 Y: 240 RGB: (  14, 208,  56)   All 4 RGB values are set to "green"  
#POS3: X:  1120 Y: 240 RGB: (  14, 208,  56)
#POS4: X:  1220 Y: 240 RGB: (  14, 208,  56)

XYcords= ((1),(2))
# I made 2 lists inside another list so I can iterate using x's and y's cords that are needed for this test.

pyautogui.FAILSAFE = True 
# When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that will abort the program.

while pyautogui.FAILSAFE == True:

    for n in cords[0][0]:
        if  pyautogui.pixelMatchesColor(100, 200, (140, 125, 134), tolerance=10) #Checks if
                pyautogui.click(x=cords[0][n], y=cords[1][n], button='left', clicks=1, interval=0.25)  # triple-click the right mouse button with a quarter second pause in between clicks








# initializing game

movements.initialize_game()
movements.do_battle()

#!/bin/python3
'''
This script can be found  https://github.com/Ctrl-Alt-Tea/AFK-Mouse-Mover
'''
import pyautogui # type: ignore
import time

SIZE_X, SIZE_Y = pyautogui.size() # Defines the screen size
 
def afkBot():
    pyautogui.moveTo(150, 150, duration = 3) 
    pyautogui.moveTo(150, 900, duration = 1) 
    pyautogui.moveTo(1700, 900, duration = 3) 
    pyautogui.moveTo(1700, 150, duration = 2) 
    pyautogui.press('space') # Used for games, for example with the above times set your character would jump every 9 seconds
    

#pyautogui.confirm('Start moving the mouse?')
#pyautogui.alert('Press Ctrl + C to stop the AFK Mouse') # Shows user how to stop

time.sleep(1) # Seconds to wait after confirming
pyautogui.moveTo(150, 150, duration = 1) 
a=1
while(a!=0):
    afkBot()  # Starts the movement
    
'''
Extra Commands should you wish to customize this:
Mouse:
  pyautogui.dragRel(100, 0, duration = 1) drags mouse 100, 0 relative to its previous position
  pyautogui.click(100, 100)
  pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
  pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
Keyboard:
  pyautogui.typewrite("Hello World !")
  pyautogui.hotkey('ctrl', 'c')  
  pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
  pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
Prompts:
  pyautogui.alert('This is an alert box.')
  pyautogui.confirm('Shall I proceed?')
  pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
  pyautogui.prompt('What is your name?')
  pyautogui.password('Enter password (text will be hidden)')
  
  
Documentation 
    # https://pyautogui.readthedocs.io/en/latest/ 
    # https://github.com/asweigart/pyautogui 

'''    

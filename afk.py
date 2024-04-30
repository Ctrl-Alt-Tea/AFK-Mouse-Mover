#!/bin/python3
import pyautogui
import time

SIZE_X, SIZE_Y = pyautogui.size()
 
def afkBot():
    pyautogui.moveTo(500, 500, duration = 1) 
    pyautogui.moveTo(500, 400, duration = 1) 
    pyautogui.moveTo(700, 400, duration = 1) 
    pyautogui.moveTo(700, 500, duration = 1) 
    #pyautogui.dragRel(100, 0, duration = 1)
    # drags mouse 100, 0 relative to its previous position, 
    # thus dragging it to 1100, 1000
    #pyautogui.dragRel(0, 100, duration = 1)
    #pyautogui.dragRel(-100, 0, duration = 1)
    #pyautogui.dragRel(0, -100, duration = 1)
    #pyautogui.click(100, 100)
    #pyautogui.typewrite("Hello World !")


a=1
time.sleep(10)
while(a!=0):
    afkBot()